from django.urls import path

from .views import HomePageView, HealthCheckView, ReadyCheckView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("health/", HealthCheckView.as_view(), name="health_check"),
    path("ready/", ReadyCheckView.as_view(), name="ready_check"),
]
