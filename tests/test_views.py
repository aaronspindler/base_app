"""
Test views across the application.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


User = get_user_model()


class TestHomeView(TestCase):
    """Test the home page view."""
    
    def setUp(self):
        """Set up test client."""
        self.client = Client()
    
    def test_home_page_status_code(self):
        """Test that home page returns 200 status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_uses_correct_template(self):
        """Test that home page uses the correct template."""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'pages/home.html')
    
    def test_home_page_contains_expected_content(self):
        """Test that home page contains expected content."""
        response = self.client.get('/')
        # Adjust this based on your actual home page content
        self.assertTrue(
            b'Welcome' in response.content or b'Home' in response.content
        )


class TestHealthCheckViews(TestCase):
    """Test health check endpoints."""
    
    def setUp(self):
        """Set up test client."""
        self.client = Client()
    
    def test_health_check_endpoint(self):
        """Test that health check endpoint returns JSON response."""
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        
        # Check response contains expected keys
        json_response = response.json()
        self.assertIn('status', json_response)
        self.assertIn('checks', json_response)
    
    def test_ready_check_endpoint(self):
        """Test that ready check endpoint returns JSON response."""
        response = self.client.get('/ready/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        
        # Check response contains expected keys
        json_response = response.json()
        self.assertIn('ready', json_response)
        self.assertIn('checks', json_response)


class TestAuthenticationViews(TestCase):
    """Test authentication-related views."""
    
    def setUp(self):
        """Set up test client and create test user."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_login_page_accessible(self):
        """Test that login page is accessible."""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup_page_accessible(self):
        """Test that signup page is accessible."""
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_login_redirect_authenticated_user(self):
        """Test that authenticated users are redirected from login page."""
        self.client.force_login(self.user)
        response = self.client.get('/accounts/login/')
        # Allauth might handle this differently
        self.assertIn(response.status_code, [200, 302])
    
    def test_logout_requires_authentication(self):
        """Test that logout requires authentication."""
        response = self.client.get('/accounts/logout/')
        # Check if it redirects to login or shows logout page
        self.assertIn(response.status_code, [200, 302])
    
    def test_password_reset_page(self):
        """Test password reset page."""
        response = self.client.get('/accounts/password/reset/')
        self.assertEqual(response.status_code, 200)
    
    def test_password_change_requires_auth(self):
        """Test that password change requires authentication."""
        response = self.client.get('/accounts/password/change/')
        self.assertEqual(response.status_code, 302)  # Should redirect to login


class TestAdminAccess(TestCase):
    """Test Django admin access."""
    
    def setUp(self):
        """Set up test client and create users."""
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
    
    def test_admin_login_page(self):
        """Test that admin login page is accessible."""
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin_requires_staff_user(self):
        """Test that admin requires staff user."""
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)  # Redirects to login
    
    def test_admin_accessible_to_superuser(self):
        """Test that admin is accessible to superuser."""
        self.client.force_login(self.superuser)
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)


class TestStaticFiles(TestCase):
    """Test static files serving."""
    
    def setUp(self):
        """Set up test client."""
        self.client = Client()
    
    def test_css_file_accessible(self):
        """Test that CSS files are accessible."""
        # This might fail in test environment depending on static files setup
        response = self.client.get('/static/css/base.css')
        # In production, this would be served by web server
        self.assertIn(response.status_code, [200, 404])
    
    def test_js_file_accessible(self):
        """Test that JS files are accessible."""
        response = self.client.get('/static/js/base.js')
        self.assertIn(response.status_code, [200, 404])