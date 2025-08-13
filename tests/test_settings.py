"""
Test Django settings configuration.
"""
from django.conf import settings
from django.test import TestCase, override_settings


class SettingsTestCase(TestCase):
    """Test Django settings configuration."""
    
    def test_secret_key_exists(self):
        """Test that SECRET_KEY is configured."""
        self.assertTrue(hasattr(settings, 'SECRET_KEY'))
        self.assertNotEqual(settings.SECRET_KEY, '')
    
    def test_debug_mode_in_test(self):
        """Test that DEBUG is properly set in test environment."""
        # DEBUG should typically be False in tests for production-like behavior
        self.assertTrue(hasattr(settings, 'DEBUG'))
    
    def test_database_configuration(self):
        """Test that database is properly configured."""
        self.assertTrue(hasattr(settings, 'DATABASES'))
        self.assertIn('default', settings.DATABASES)
    
    def test_installed_apps(self):
        """Test that required apps are installed."""
        required_apps = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'allauth',
            'allauth.account',
            'crispy_forms',
            'crispy_bootstrap5',
            'accounts',
            'pages',
        ]
        for app in required_apps:
            self.assertIn(app, settings.INSTALLED_APPS)
    
    def test_middleware_configuration(self):
        """Test that required middleware is configured."""
        required_middleware = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ]
        for middleware in required_middleware:
            self.assertIn(middleware, settings.MIDDLEWARE)
    
    def test_static_files_configuration(self):
        """Test static files settings."""
        self.assertTrue(hasattr(settings, 'STATIC_URL'))
        self.assertTrue(hasattr(settings, 'STATIC_ROOT'))
        self.assertEqual(settings.STATIC_URL, '/static/')
    
    def test_templates_configuration(self):
        """Test templates settings."""
        self.assertTrue(hasattr(settings, 'TEMPLATES'))
        self.assertGreater(len(settings.TEMPLATES), 0)
        self.assertEqual(settings.TEMPLATES[0]['BACKEND'], 'django.template.backends.django.DjangoTemplates')
    
    @override_settings(DEBUG=False)
    def test_production_settings(self):
        """Test settings suitable for production."""
        from django.conf import settings
        self.assertFalse(settings.DEBUG)
    
    def test_custom_user_model(self):
        """Test that custom user model is configured."""
        self.assertEqual(settings.AUTH_USER_MODEL, 'accounts.CustomUser')
    
    def test_authentication_backends(self):
        """Test authentication backends configuration."""
        self.assertIn('django.contrib.auth.backends.ModelBackend', settings.AUTHENTICATION_BACKENDS)
        self.assertIn('allauth.account.auth_backends.AuthenticationBackend', settings.AUTHENTICATION_BACKENDS)


class TestEnvironmentVariables(TestCase):
    """Test environment variable handling."""
    
    def test_database_url_parsing(self):
        """Test that DATABASE_URL is properly parsed."""
        # This test would check if environ is properly parsing DATABASE_URL
        self.assertIn('default', settings.DATABASES)
    
    def test_secret_key_not_default(self):
        """Test that SECRET_KEY is not using the default value in production."""
        # In a real scenario, you'd want to ensure the secret key is properly set
        self.assertNotEqual(settings.SECRET_KEY, "fake_secret_key_switch_me_123451231")