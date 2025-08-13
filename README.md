# 🚀 Django Template Repository

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Django](https://img.shields.io/badge/Django-5.1%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)
![Code Style](https://img.shields.io/badge/Code%20Style-Black%20%26%20Ruff-black)
![Test Coverage](https://img.shields.io/badge/Coverage-90%25%2B-brightgreen)

A modern, production-ready Django template with best practices, automated testing, and continuous integration built-in. Perfect for quickly starting new Django projects with a solid foundation.

![](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHB5ZGdsYjdjeDRiM21xNWoxbXFxb291M2x1M24xb200cWxtOHdtNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R5Q7WDoNYKgg37V9LX/giphy.gif)

## ✨ Features

### 🏗️ Core Features
- **Django 5.1+** with PostgreSQL database support
- **Custom User Model** ready for extension
- **Django Allauth** for comprehensive authentication (email-based)
- **Bootstrap 5** with Crispy Forms for beautiful UI
- **WhiteNoise** for efficient static file serving
- **Health Check Endpoints** (`/health/` and `/ready/`)
- **Environment-based configuration** with django-environ
- **Comprehensive error pages** (404, 500, CSRF)

### 🔧 Development Tools
- **Pre-configured Makefile** with 50+ useful commands
- **Pre-commit hooks** for automated code quality checks
- **Comprehensive testing setup** with pytest and coverage reporting
- **Code formatting** with Black, isort, and Ruff
- **Type checking** with MyPy and django-stubs
- **Security scanning** with Bandit, Safety, and pip-audit
- **VS Code** and **EditorConfig** configurations included
- **Docker** and **Docker Compose** for containerized development
- **Django Debug Toolbar** for development insights
- **IPython** and **django-extensions** for enhanced shell experience

### 🚀 CI/CD & Automation
- **GitHub Actions workflows** for automated testing and deployment
- **Dependabot** for automated dependency updates with auto-merge
- **Multi-version testing** (Python 3.11, 3.12, 3.13)
- **PostgreSQL testing** with service containers
- **Code quality checks** on every pull request
- **Coverage reporting** with Codecov integration
- **Production deployment ready** with CapRover support
- **Reusable workflow architecture** for efficiency

### 📝 Project Templates & Documentation
- **GitHub Issue Templates** for bugs and feature requests
- **Pull Request Template** with comprehensive checklist
- **Contributing Guidelines** with detailed instructions
- **Security Policy** with vulnerability reporting process
- **MIT License** for open-source flexibility
- **Comprehensive inline documentation**

## 🎯 Quick Start

### Prerequisites
- Python 3.11+ (3.13.1 recommended)
- PostgreSQL 15+ (or Docker for containerized setup)
- Git
- Make (optional but recommended)

### 🚀 Option 1: Local Development

1. **Clone and setup the repository:**
```bash
# Clone the repository
git clone https://github.com/yourusername/base_app.git
cd base_app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
make install  # Or: pip install -r requirements.txt -r requirements-dev.txt
```

2. **Configure environment:**
```bash
# Create .env file with your configuration
cat > .env << EOF
# Django Settings
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True

# Database Configuration
# For SQLite (development):
DATABASE_URL=sqlite:///db.sqlite3
# For PostgreSQL (recommended):
# DATABASE_URL=postgres://user:password@localhost:5432/dbname

# Optional: Redis Cache
# REDIS_URL=redis://localhost:6379/1

# Optional: Email (for development, use console backend)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EOF

# Generate a secure secret key for production:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

3. **Setup database:**
```bash
# Run migrations
make migrate  # Or: python manage.py migrate

# Create superuser
make superuser  # Or: python manage.py createsuperuser

# Collect static files
make collectstatic  # Or: python manage.py collectstatic --noinput
```

4. **Run the development server:**
```bash
make run  # Or: python manage.py runserver
```

Visit http://localhost:8000 to see your app!

### 🐳 Option 2: Docker Development

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/base_app.git
cd base_app
```

2. **Build and run with Docker Compose:**
```bash
# Build and start all services
docker-compose up --build

# In another terminal, run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

Visit:
- **App**: http://localhost:8000
- **Adminer** (Database UI): http://localhost:8080
- **Mailhog** (Email testing): http://localhost:8025

## 📚 Project Structure

```
base_app/
├── .github/                # GitHub Actions workflows and templates
│   ├── workflows/          # CI/CD pipelines
│   │   ├── test-and-check.yml      # Reusable test workflow
│   │   ├── test_and_deploy.yml     # Main CI/CD workflow
│   │   ├── code-quality.yml        # Code quality checks
│   │   └── dependabot-auto-merge.yml # Auto-merge dependencies
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   ├── scripts/            # Setup and utility scripts
│   └── pull_request_template.md
├── accounts/               # Custom user model app
│   ├── models.py          # User model customizations
│   ├── forms.py           # Authentication forms
│   └── admin.py           # Admin interface setup
├── config/                 # Django project configuration
│   ├── settings.py        # Main settings file
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── pages/                  # Static pages app
│   ├── views.py           # Page views
│   └── urls.py            # Page routing
├── static/                 # Static assets
│   ├── css/               # Stylesheets
│   └── js/                # JavaScript files
├── templates/              # HTML templates
│   ├── _base.html         # Base template
│   ├── account/           # Authentication templates
│   └── pages/             # Page templates
├── tests/                  # Test suite
│   ├── test_views.py      # View tests
│   └── test_settings.py   # Settings tests
├── .vscode/                # VS Code configuration
├── docker-compose.yml      # Docker development setup
├── docker-compose.prod.yml # Production Docker setup
├── Dockerfile              # Container definition
├── Makefile                # Development commands
├── pyproject.toml          # Python project configuration
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── ruff.toml              # Ruff linter configuration
└── manage.py              # Django management script
```

## 🛠️ Development

### Common Commands

The Makefile provides 50+ useful commands for development:

```bash
# Setup & Installation
make install            # Install all dependencies
make setup             # Complete initial setup
make venv              # Create virtual environment

# Database Management
make migrate           # Run migrations
make makemigrations    # Create new migrations
make superuser         # Create superuser account
make shell            # Django shell with IPython
make dbshell          # Database shell

# Development Server
make run              # Run development server
make run-plus         # Run with Werkzeug debugger

# Testing
make test             # Run all tests
make test-coverage    # Run tests with coverage report
make test-fast        # Run tests in parallel
make test-unit        # Run unit tests only
make test-integration # Run integration tests only

# Code Quality
make lint             # Run all linters
make format           # Format code automatically
make ruff             # Run Ruff linter
make black            # Format with Black
make isort            # Sort imports
make mypy             # Type checking
make security         # Security checks
make pre-commit       # Run pre-commit hooks

# Docker Commands
make docker-build     # Build Docker image
make docker-up        # Start containers
make docker-down      # Stop containers
make docker-logs      # View logs
make docker-shell     # Shell into container
make docker-clean     # Clean Docker resources

# Utilities
make clean            # Clean generated files
make urls             # Show URL patterns
make find-todos       # Find TODO comments
make deploy-check     # Check deployment readiness

# Show all available commands
make help
```

### Pre-commit Hooks

Pre-commit hooks ensure code quality before commits:

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Update hook versions
pre-commit autoupdate
```

Configured hooks include:
- **Black** - Code formatting
- **isort** - Import sorting
- **Ruff** - Linting
- **MyPy** - Type checking
- **Bandit** - Security analysis
- **Check for merge conflicts**
- **Debug statement detection**
- **Large file prevention**

### Running Tests

```bash
# Run with pytest (recommended)
pytest                      # Run all tests
pytest --cov               # With coverage
pytest -n auto             # Run in parallel
pytest -x                  # Stop on first failure
pytest --lf                # Run last failed
pytest -k test_name        # Run specific test

# Run with Django test runner
python manage.py test

# Coverage reports
make test-coverage         # Generate coverage report
coverage html             # Generate HTML report
open htmlcov/index.html   # View report
```

### Code Style & Quality

This project enforces strict code quality standards:

- **Black**: Code formatting (line length: 88)
- **isort**: Import organization
- **Ruff**: Fast Python linting
- **MyPy**: Static type checking
- **Bandit**: Security vulnerability scanning

Configuration is centralized in `pyproject.toml` and `ruff.toml`.

## 🚀 GitHub Workflows

### Continuous Integration

The project includes several GitHub Actions workflows:

#### 1. **Test and Deploy** (`test_and_deploy.yml`)
- Triggers on pushes and PRs to main
- Runs comprehensive test suite
- Checks code quality
- Ready for deployment (disabled by default)

#### 2. **Reusable Test Workflow** (`test-and-check.yml`)
- Configurable Python version (3.11-3.13)
- PostgreSQL service container
- Coverage reporting
- Security checks
- Migration validation

#### 3. **Code Quality** (`code-quality.yml`)
- Linting with Ruff, Black, isort
- Type checking with MyPy
- Security scanning with Bandit
- Runs on all PRs

#### 4. **Dependabot Auto-Merge** (`dependabot-auto-merge.yml`)
- Auto-merges minor and patch updates
- Requires passing tests
- Manual review for major updates
- Security updates prioritized

### 🏷️ Required GitHub Setup

**One-time setup required** for GitHub labels:

```bash
# Quick setup (recommended)
chmod +x .github/scripts/setup-labels.sh
./.github/scripts/setup-labels.sh

# Or for Windows PowerShell
.\.github\scripts\setup-labels.ps1
```

Required labels:
- `auto-merge` - For automatic dependency merging
- `security` - Security-related updates
- `dependencies` - Dependency updates
- `python` - Python-related changes
- `github-actions` - Workflow updates
- `docker` - Container-related changes

## 🔧 Environment Variables

The application uses environment variables for configuration. Create a `.env` file in the project root:

### Core Settings
```bash
# Django Settings
SECRET_KEY=your-secret-key-here              # REQUIRED: Generate new for production
DEBUG=True                                    # Set to False in production

# Database
DATABASE_URL=postgres://user:pass@localhost:5432/db  # PostgreSQL
# DATABASE_URL=sqlite:///db.sqlite3          # SQLite (development only)

# Cache (optional)
REDIS_URL=redis://localhost:6379/1           # Redis cache backend
```

### Email Configuration
```bash
# SMTP Settings (Production)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Development (console output)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### Security Settings (Production)
```bash
# HTTPS and Security Headers
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True

# Allowed Hosts
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

### External Services (Optional)
```bash
# AWS S3 for Static/Media Files
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=us-east-1

# Error Tracking
SENTRY_DSN=https://your-key@sentry.io/project-id

# Analytics
GOOGLE_ANALYTICS_ID=UA-XXXXXXXXX-X
GOOGLE_TAG_MANAGER_ID=GTM-XXXXXXX
```

### Feature Flags
```bash
# Application Features
ENABLE_REGISTRATION=True
ENABLE_SOCIAL_AUTH=False
MAINTENANCE_MODE=False
LOG_LEVEL=INFO
```

## 🔒 Security

### Built-in Security Features

- **Django Security Middleware** enabled by default
- **CSRF Protection** on all forms
- **XSS Protection** via Django's template system
- **SQL Injection Protection** through ORM usage
- **Secure Password Hashing** with PBKDF2
- **Security Headers** configured for production
- **Rate Limiting** ready to implement
- **Automated Security Scanning** in CI/CD

### Security Best Practices

1. **Environment Variables**
   - Never commit `.env` files
   - Use strong `SECRET_KEY` in production
   - Rotate credentials regularly

2. **Production Settings**
   - Set `DEBUG=False`
   - Configure `ALLOWED_HOSTS`
   - Enable HTTPS with proper certificates
   - Use secure cookie settings

3. **Dependencies**
   - Regular updates via Dependabot
   - Security scanning with Safety and pip-audit
   - Monitor CVE databases

### Reporting Security Issues

See [SECURITY.md](SECURITY.md) for vulnerability reporting guidelines.

## 🚢 Deployment

### Production Checklist

Before deploying to production:

```bash
# Run Django's deployment check
python manage.py check --deploy

# Or use Makefile
make deploy-check
```

Essential production settings:
- [ ] `DEBUG = False`
- [ ] Strong `SECRET_KEY` (generate new one)
- [ ] `ALLOWED_HOSTS` configured
- [ ] Database backups configured
- [ ] SSL/HTTPS enabled
- [ ] Static files properly served
- [ ] Email backend configured
- [ ] Error tracking (e.g., Sentry) set up
- [ ] Monitoring and logging configured

### Deployment Options

#### CapRover Deployment

1. **Enable deployment** in `.github/workflows/test_and_deploy.yml`
2. **Configure GitHub secrets**:
   - `NEW_CAPROVER_SERVER`
   - `CAPROVER_WEB_APP_NAME`
   - `NEW_CAPROVER_WEB_APP_TOKEN`
   - `DATABASE_URL`
   - `SECRET_KEY`
   - `PRODUCTION_URL`

#### Docker Production

```bash
# Build production image
docker build -t base_app:prod \
  --build-arg DATABASE_URL=$DATABASE_URL \
  --build-arg SECRET_KEY=$SECRET_KEY \
  --build-arg DEBUG=False .

# Run production container
docker run -d -p 80:80 base_app:prod
```

#### Traditional Deployment

1. Install dependencies: `pip install -r requirements.txt`
2. Set environment variables
3. Run migrations: `python manage.py migrate`
4. Collect static files: `python manage.py collectstatic`
5. Configure web server (Nginx/Apache)
6. Setup WSGI server (Gunicorn/uWSGI)

## 📊 Monitoring & Health Checks

### Health Check Endpoints

The application provides health monitoring endpoints:

#### `/health/` - Application Health
```json
{
  "status": "healthy",
  "checks": {
    "database": {
      "status": "healthy",
      "message": "Database connection successful"
    },
    "cache": {
      "status": "healthy",
      "message": "Cache is operational"
    },
    "disk_space": {
      "status": "healthy",
      "message": "Disk space available: 45.2%"
    },
    "memory": {
      "status": "healthy",
      "message": "Memory usage: 62.1%"
    }
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### `/ready/` - Readiness Check
Verifies the application is ready to serve traffic:
- Database migrations applied
- Static files collected
- All services initialized

### Performance Monitoring

The template includes tools for performance analysis:

- **Django Debug Toolbar** - Development profiling
- **django-silk** - Request/response profiling
- **django-querycount** - Database query monitoring
- **py-spy** - Python profiling
- **memory-profiler** - Memory usage analysis

## 🔄 Staying Up to Date

This template is designed for minimal maintenance:

### Automated Updates
- **Dependabot** creates PRs for dependency updates
- **Auto-merge** for minor/patch versions
- **Security updates** prioritized
- **GitHub Actions** stay current

### Manual Updates
```bash
# Update Python dependencies
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt

# Update pre-commit hooks
pre-commit autoupdate

# Update npm packages (if any)
npm update

# Check for Django updates
pip list --outdated
```

## 💡 Tips for Using This Template

### Starting a New Project

1. **Use GitHub's template feature** or clone the repository
2. **Search and replace** `base_app` with your project name
3. **Update project metadata** in `pyproject.toml`
4. **Configure your domain** in settings
5. **Set up GitHub labels** using the provided script
6. **Customize the user model** early if needed
7. **Remove example apps** if not needed
8. **Update this README** for your specific project

### Customization Points

- **User Model**: Extend in `accounts/models.py`
- **Authentication**: Configure in `config/settings.py`
- **Static Files**: Customize in `static/` directory
- **Templates**: Base template in `templates/_base.html`
- **URL Routing**: Main routes in `config/urls.py`
- **Admin Interface**: Customize in `accounts/admin.py`

### Best Practices

1. **Keep dependencies updated** regularly
2. **Write tests** for all new features
3. **Use feature branches** for development
4. **Document API changes** thoroughly
5. **Follow commit conventions** (conventional commits)
6. **Review security advisories** promptly
7. **Monitor application logs** in production

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code of conduct
- Development setup instructions
- Coding standards and style guide
- Pull request process
- Testing guidelines
- Documentation requirements

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This template incorporates best practices from:
- [Django Documentation](https://docs.djangoproject.com/)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [Django Best Practices](https://djangobestpractices.com/)
- [12 Factor App](https://12factor.net/)
- The amazing Django community

## 🆘 Support & Resources

### Getting Help
- **Issues**: [GitHub Issues](https://github.com/yourusername/base_app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/base_app/discussions)
- **Security**: See [SECURITY.md](SECURITY.md)
- **Django Docs**: [djangoproject.com](https://www.djangoproject.com/)

### Useful Links
- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [Django Packages](https://djangopackages.org/)
- [Awesome Django](https://github.com/wsvincent/awesome-django)
- [Django Forum](https://forum.djangoproject.com/)
- [Django Discord](https://discord.gg/xcRH6mN4fa)

### Troubleshooting

Common issues and solutions:

**Database connection errors:**
```bash
# Check PostgreSQL is running
pg_isready

# Verify DATABASE_URL format
echo $DATABASE_URL
```

**Static files not loading:**
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check STATIC_ROOT setting
python manage.py shell -c "from django.conf import settings; print(settings.STATIC_ROOT)"
```

**Migration issues:**
```bash
# Check migration status
python manage.py showmigrations

# Reset migrations (development only)
python manage.py migrate --fake-initial
```

---

<div align="center">

**Built with ❤️ using Django**

If you find this template useful, please give it a ⭐️

[Report Bug](https://github.com/yourusername/base_app/issues) · [Request Feature](https://github.com/yourusername/base_app/issues) · [Contribute](CONTRIBUTING.md)

</div>