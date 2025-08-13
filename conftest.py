"""
Pytest configuration and fixtures for the entire test suite.
"""
import os
import sys
from pathlib import Path

import django
import pytest
from django.conf import settings
from django.test import TransactionTestCase

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Setup Django settings before importing any Django modules
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def pytest_configure(config):
    """Configure pytest with Django settings."""
    if not settings.configured:
        django.setup()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """
    Automatically enable database access for all tests.
    
    This fixture ensures that all tests have database access by default,
    eliminating the need to mark each test with @pytest.mark.django_db.
    """
    pass


@pytest.fixture
def client():
    """Return a Django test client instance."""
    from django.test import Client
    return Client()


@pytest.fixture
def admin_client(db):
    """Return a Django admin client instance."""
    from django.contrib.auth import get_user_model
    from django.test import Client
    
    User = get_user_model()
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123'
    )
    client = Client()
    client.force_login(admin_user)
    return client


@pytest.fixture
def user(db):
    """Create and return a test user."""
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )


@pytest.fixture
def authenticated_client(client, user):
    """Return an authenticated client."""
    client.force_login(user)
    return client


@pytest.fixture
def api_client():
    """Return a Django REST framework API client if installed."""
    try:
        from rest_framework.test import APIClient
        return APIClient()
    except ImportError:
        pytest.skip("Django REST Framework not installed")


@pytest.fixture
def mock_redis(mocker):
    """Mock Redis client for tests."""
    mock = mocker.patch('redis.StrictRedis')
    return mock


@pytest.fixture
def mock_celery_task(mocker):
    """Mock Celery task execution."""
    mock = mocker.patch('celery.Task.apply_async')
    return mock


@pytest.fixture
def settings_override():
    """
    Context manager for temporarily overriding Django settings.
    
    Usage:
        def test_something(settings_override):
            with settings_override(DEBUG=False):
                # test code here
    """
    from django.test import override_settings
    return override_settings


@pytest.fixture
def mailoutbox(settings):
    """Provide access to Django's test email outbox."""
    from django.core import mail
    
    # Clear the outbox before each test
    mail.outbox.clear()
    
    # Set email backend to locmem for testing
    settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
    
    return mail.outbox


@pytest.fixture
def temp_media_root(tmp_path, settings):
    """Create a temporary media root for file upload tests."""
    media_root = tmp_path / "media"
    media_root.mkdir()
    settings.MEDIA_ROOT = str(media_root)
    return media_root


# Markers for organizing tests
pytest.mark.unit = pytest.mark.mark(name="unit")
pytest.mark.integration = pytest.mark.mark(name="integration")
pytest.mark.slow = pytest.mark.mark(name="slow")
pytest.mark.smoke = pytest.mark.mark(name="smoke")


class TestCase(TransactionTestCase):
    """Base test case class with additional utilities."""
    
    def assertRedirects(self, response, expected_url, status_code=302):
        """Assert that a response redirects to the expected URL."""
        assert response.status_code == status_code
        assert response.url == expected_url
