# 🚀 Django Template Repository

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Django](https://img.shields.io/badge/Django-5.1%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-black)

A modern, production-ready Django template with best practices, automated testing, and continuous integration built-in. Perfect for quickly starting new Django projects with a solid foundation.

![](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHB5ZGdsYjdjeDRiM21xNWoxbXFxb291M2x1M24xb200cWxtOHdtNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R5Q7WDoNYKgg37V9LX/giphy.gif)

## ✨ Features

### 🏗️ Core Features
- **Django 5.1+** with PostgreSQL database
- **Custom User Model** ready for extension
- **Django Allauth** for authentication (email-based)
- **Bootstrap 5** with Crispy Forms
- **WhiteNoise** for static file serving
- **Health Check Endpoints** (`/health/` and `/ready/`)
- **Environment-based configuration** with django-environ

### 🔧 Development Tools
- **Pre-commit hooks** for code quality
- **Comprehensive testing** with pytest
- **Code formatting** with Black, isort, and Ruff
- **Type checking** with MyPy
- **Security scanning** with Bandit and Safety
- **VS Code** and **EditorConfig** configurations
- **Makefile** for common commands
- **Docker** and **Docker Compose** support

### 🚀 CI/CD & Automation
- **GitHub Actions** workflows for testing and deployment
- **Dependabot** for automated dependency updates
- **Auto-merge** for minor/patch updates
- **Code quality checks** on every PR
- **Coverage reporting** with Codecov support
- **Production deployment** ready (disabled by default)

### 📝 Documentation & Templates
- **GitHub Issue Templates** for bugs and features
- **Pull Request Template** with checklist
- **Contributing Guidelines**
- **Security Policy**
- **MIT License**

## 🎯 Quick Start

### Prerequisites
- Python 3.11+ (3.13.1 recommended)
- PostgreSQL 15+ (or Docker)
- Git

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
# Copy environment template
cp .env.template .env

# Edit .env with your settings (especially DATABASE_URL)
# For local PostgreSQL:
# DATABASE_URL=postgres://user:password@localhost:5432/dbname
# For SQLite (development only):
# DATABASE_URL=sqlite:///db.sqlite3
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
- App: http://localhost:8000
- Adminer (DB management): http://localhost:8080
- Mailhog (email testing): http://localhost:8025

## 📚 Project Structure

```
base_app/
├── .github/                # GitHub Actions workflows and templates
│   ├── workflows/          # CI/CD workflows
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   └── scripts/            # Setup scripts
├── accounts/               # Custom user model app
├── config/                 # Django settings and configuration
├── pages/                  # Static pages app
├── static/                 # Static files (CSS, JS)
├── templates/              # HTML templates
├── tests/                  # Test suite
├── .vscode/                # VS Code settings
├── docker-compose.yml      # Docker development setup
├── Dockerfile              # Container definition
├── Makefile                # Common commands
├── pyproject.toml          # Python project configuration
├── requirements.txt        # Production dependencies
└── requirements-dev.txt    # Development dependencies
```

## 🛠️ Development

### Common Commands

```bash
# Testing
make test                # Run all tests
make test-coverage       # Run tests with coverage
make test-fast          # Run tests in parallel

# Code Quality
make lint               # Run all linters
make format             # Format code with black and isort
make security           # Run security checks

# Database
make migrate            # Run migrations
make makemigrations     # Create new migrations
make shell              # Django shell (with ipython if available)

# Docker
make docker-build       # Build Docker image
make docker-up          # Start containers
make docker-down        # Stop containers

# See all commands
make help
```

### Pre-commit Hooks

Install pre-commit hooks to ensure code quality:
```bash
pre-commit install
pre-commit run --all-files  # Run on all files
```

### Running Tests

```bash
# With pytest (recommended)
pytest
pytest --cov  # With coverage
pytest -n auto  # Run in parallel

# With Django test runner
python manage.py test
```

### Code Style

This project uses:
- **Black** for Python formatting (line length: 88)
- **isort** for import sorting
- **Ruff** for linting
- **MyPy** for type checking

All configured in `pyproject.toml` and enforced by pre-commit hooks.

## 🚀 GitHub Workflows

### Available Workflows

1. **Test and Deploy** (`test_and_deploy.yml`)
   - Runs on every push and PR to main
   - Tests with PostgreSQL
   - Coverage reporting
   - Deployment ready (disabled by default)

2. **Code Quality** (`code-quality.yml`)
   - Linting with Ruff, Black, isort
   - Type checking with MyPy
   - Security scanning

3. **Dependabot Auto-Merge** (`dependabot-auto-merge.yml`)
   - Auto-merges minor/patch updates
   - Requires manual review for major updates
   - Security updates prioritized

4. **Reusable Test Workflow** (`test-and-check.yml`)
   - Shared testing logic
   - Configurable Python/PostgreSQL versions

### 🏷️ Required Setup: GitHub Labels

**The only manual setup required** is creating GitHub labels for Dependabot:

```bash
# Quick setup (recommended)
chmod +x .github/scripts/setup-labels.sh
./.github/scripts/setup-labels.sh
```

Or create manually in GitHub Settings → Labels:
- `auto-merge` (color: #0E8A16)
- `security` (color: #D93F0B)
- `dependencies` (color: #0366D6)
- `python` (color: #3776AB)
- `github-actions` (color: #2088FF)
- `docker` (color: #2496ED)

## 🔒 Security

### Security Features
- Django security middleware enabled
- CSRF protection
- XSS protection via templates
- SQL injection protection via ORM
- Secure password hashing
- Security headers for production
- Automated security scanning

### Environment Variables
- Never commit `.env` files
- Use strong `SECRET_KEY` in production
- Set `DEBUG=False` in production
- Configure `ALLOWED_HOSTS` properly

### Reporting Security Issues
See [SECURITY.md](SECURITY.md) for our security policy.

## 🚢 Deployment

### Enabling Deployment

1. **Uncomment deployment job** in `.github/workflows/test_and_deploy.yml`

2. **Configure secrets** in GitHub repository settings:
   - `DATABASE_URL`
   - `SECRET_KEY`
   - For CapRover:
     - `NEW_CAPROVER_SERVER`
     - `CAPROVER_WEB_APP_NAME`
     - `NEW_CAPROVER_WEB_APP_TOKEN`
     - `PRODUCTION_URL`

3. **Update production settings** in `config/settings.py`:
   - Add your domain to `ALLOWED_HOSTS`
   - Configure `CSRF_TRUSTED_ORIGINS`
   - Set up email backend
   - Configure static/media file storage

### Production Checklist

```bash
# Run Django's deployment check
python manage.py check --deploy

# Or use Makefile
make deploy-check
```

Ensure:
- [ ] `DEBUG = False`
- [ ] Strong `SECRET_KEY`
- [ ] Database backups configured
- [ ] SSL/HTTPS enabled
- [ ] Static files served properly
- [ ] Error tracking (e.g., Sentry) configured
- [ ] Monitoring and logging set up

## 📊 Monitoring

### Health Check Endpoints

- **`/health/`** - Application health status
  - Database connectivity
  - Cache status
  - Disk space
  - Memory usage
  
- **`/ready/`** - Readiness check
  - Migration status
  - Static files collected

Example response:
```json
{
  "status": "healthy",
  "checks": {
    "database": {"status": "healthy", "message": "Database connection successful"},
    "cache": {"status": "healthy", "message": "Cache is operational"},
    "disk_space": {"status": "healthy", "message": "Disk space available: 45.2%"},
    "memory": {"status": "healthy", "message": "Memory usage: 62.1%"}
  }
}
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code of conduct
- Development setup
- Coding standards
- Pull request process
- Testing guidelines

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This template incorporates best practices from:
- [Django Documentation](https://docs.djangoproject.com/)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [Django Best Practices](https://djangobestpractices.com/)
- The amazing Django community

## 🔄 Staying Up to Date

This template is designed to stay current with minimal maintenance:

1. **Automated dependency updates** via Dependabot
2. **Pre-commit hook updates** via `pre-commit autoupdate`
3. **Python version** specified in `.python-version`
4. **GitHub Actions** use latest stable versions
5. **Security scanning** catches vulnerabilities

To update manually:
```bash
# Update dependencies
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt

# Update pre-commit hooks
pre-commit autoupdate

# Update GitHub Actions (automatic via Dependabot)
```

## 💡 Tips for Template Usage

When using this template for a new project:

1. **Search and replace** `base_app` with your project name
2. **Update** `SECRET_KEY` in production
3. **Configure** your specific `ALLOWED_HOSTS`
4. **Set up** GitHub labels (run setup script)
5. **Customize** the user model early if needed
6. **Remove** example apps if not needed
7. **Update** this README for your project

## 🆘 Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourusername/base_app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/base_app/discussions)
- **Security**: See [SECURITY.md](SECURITY.md)
- **Django Docs**: [djangoproject.com](https://www.djangoproject.com/)

---

**Happy coding!** 🚀 If you find this template useful, please give it a ⭐️