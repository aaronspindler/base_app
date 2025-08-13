import json
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View
from django.db import connection
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class HealthCheckView(View):
    """
    Health check endpoint for monitoring.
    Returns JSON response with system status.
    """
    
    def get(self, request, *args, **kwargs):
        health_status = {
            "status": "healthy",
            "checks": {}
        }
        
        # Database check
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                cursor.fetchone()
            health_status["checks"]["database"] = {
                "status": "healthy",
                "message": "Database connection successful"
            }
        except Exception as e:
            health_status["status"] = "unhealthy"
            health_status["checks"]["database"] = {
                "status": "unhealthy",
                "message": str(e)
            }
            logger.error(f"Database health check failed: {e}")
        
        # Cache check (if configured)
        try:
            cache.set('health_check', 'ok', 1)
            if cache.get('health_check') == 'ok':
                health_status["checks"]["cache"] = {
                    "status": "healthy",
                    "message": "Cache is operational"
                }
            else:
                health_status["checks"]["cache"] = {
                    "status": "warning",
                    "message": "Cache set/get mismatch"
                }
        except Exception as e:
            health_status["checks"]["cache"] = {
                "status": "warning",
                "message": f"Cache not configured or unavailable: {e}"
            }
        
        # Disk space check
        import shutil
        try:
            disk_usage = shutil.disk_usage("/")
            disk_free_percentage = (disk_usage.free / disk_usage.total) * 100
            
            if disk_free_percentage > 20:
                health_status["checks"]["disk_space"] = {
                    "status": "healthy",
                    "message": f"Disk space available: {disk_free_percentage:.1f}%"
                }
            elif disk_free_percentage > 10:
                health_status["checks"]["disk_space"] = {
                    "status": "warning",
                    "message": f"Low disk space: {disk_free_percentage:.1f}%"
                }
            else:
                health_status["status"] = "unhealthy"
                health_status["checks"]["disk_space"] = {
                    "status": "unhealthy",
                    "message": f"Critical disk space: {disk_free_percentage:.1f}%"
                }
        except Exception as e:
            health_status["checks"]["disk_space"] = {
                "status": "unknown",
                "message": str(e)
            }
        
        # Memory check
        import psutil
        try:
            memory = psutil.virtual_memory()
            if memory.percent < 80:
                health_status["checks"]["memory"] = {
                    "status": "healthy",
                    "message": f"Memory usage: {memory.percent:.1f}%"
                }
            elif memory.percent < 90:
                health_status["checks"]["memory"] = {
                    "status": "warning",
                    "message": f"High memory usage: {memory.percent:.1f}%"
                }
            else:
                health_status["status"] = "unhealthy"
                health_status["checks"]["memory"] = {
                    "status": "unhealthy",
                    "message": f"Critical memory usage: {memory.percent:.1f}%"
                }
        except ImportError:
            health_status["checks"]["memory"] = {
                "status": "unknown",
                "message": "psutil not installed"
            }
        except Exception as e:
            health_status["checks"]["memory"] = {
                "status": "unknown",
                "message": str(e)
            }
        
        # Determine HTTP status code
        if health_status["status"] == "unhealthy":
            status_code = 503
        else:
            status_code = 200
        
        return JsonResponse(health_status, status=status_code)


class ReadyCheckView(View):
    """
    Readiness check endpoint for container orchestration.
    Checks if the application is ready to serve requests.
    """
    
    def get(self, request, *args, **kwargs):
        ready_status = {
            "ready": True,
            "checks": {}
        }
        
        # Check database migrations
        try:
            from django.core.management import call_command
            from io import StringIO
            output = StringIO()
            call_command('showmigrations', '--plan', stdout=output)
            ready_status["checks"]["migrations"] = {
                "status": "ready",
                "message": "All migrations applied"
            }
        except Exception as e:
            ready_status["ready"] = False
            ready_status["checks"]["migrations"] = {
                "status": "not_ready",
                "message": str(e)
            }
        
        # Check static files
        from django.conf import settings
        import os
        if os.path.exists(settings.STATIC_ROOT):
            ready_status["checks"]["static_files"] = {
                "status": "ready",
                "message": "Static files collected"
            }
        else:
            ready_status["checks"]["static_files"] = {
                "status": "warning",
                "message": "Static files not collected"
            }
        
        status_code = 200 if ready_status["ready"] else 503
        return JsonResponse(ready_status, status=status_code)
