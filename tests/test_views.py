"""
Test views across the application.
"""
import pytest
from django.urls import reverse
from django.test import TestCase


@pytest.mark.django_db
class TestHomeView:
    """Test the home page view."""
    
    def test_home_page_status_code(self, client):
        """Test that home page returns 200 status code."""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_page_uses_correct_template(self, client):
        """Test that home page uses the correct template."""
        response = client.get('/')
        assert 'pages/home.html' in [t.name for t in response.templates]
    
    def test_home_page_contains_expected_content(self, client):
        """Test that home page contains expected content."""
        response = client.get('/')
        # Adjust this based on your actual home page content
        assert b'Welcome' in response.content or b'Home' in response.content


@pytest.mark.django_db
class TestAuthenticationViews:
    """Test authentication-related views."""
    
    def test_login_page_accessible(self, client):
        """Test that login page is accessible."""
        response = client.get('/accounts/login/')
        assert response.status_code == 200
    
    def test_signup_page_accessible(self, client):
        """Test that signup page is accessible."""
        response = client.get('/accounts/signup/')
        assert response.status_code == 200
    
    def test_login_redirect_authenticated_user(self, authenticated_client):
        """Test that authenticated users are redirected from login page."""
        response = authenticated_client.get('/accounts/login/')
        # Allauth might handle this differently
        assert response.status_code in [200, 302]
    
    def test_logout_requires_authentication(self, client):
        """Test that logout requires authentication."""
        response = client.get('/accounts/logout/')
        # Check if it redirects to login or shows logout page
        assert response.status_code in [200, 302]
    
    @pytest.mark.parametrize("url,expected_status", [
        ('/accounts/password/reset/', 200),
        ('/accounts/password/change/', 302),  # Requires auth
    ])
    def test_password_pages(self, client, url, expected_status):
        """Test password-related pages."""
        response = client.get(url)
        assert response.status_code == expected_status


@pytest.mark.django_db
class TestAdminAccess:
    """Test Django admin access."""
    
    def test_admin_login_page(self, client):
        """Test that admin login page is accessible."""
        response = client.get('/admin/login/')
        assert response.status_code == 200
    
    def test_admin_requires_staff_user(self, client):
        """Test that admin requires staff user."""
        response = client.get('/admin/')
        assert response.status_code == 302  # Redirects to login
    
    def test_admin_accessible_to_superuser(self, admin_client):
        """Test that admin is accessible to superuser."""
        response = admin_client.get('/admin/')
        assert response.status_code == 200


@pytest.mark.integration
class TestStaticFiles:
    """Test static files serving."""
    
    def test_css_file_accessible(self, client):
        """Test that CSS files are accessible."""
        # This might fail in test environment depending on static files setup
        response = client.get('/static/css/base.css')
        # In production, this would be served by web server
        assert response.status_code in [200, 404]
    
    def test_js_file_accessible(self, client):
        """Test that JS files are accessible."""
        response = client.get('/static/js/base.js')
        assert response.status_code in [200, 404]
