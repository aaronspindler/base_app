# base_app
![](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHB5ZGdsYjdjeDRiM21xNWoxbXFxb291M2x1M24xb200cWxtOHdtNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R5Q7WDoNYKgg37V9LX/giphy.gif)

This is my base cookiecutter django setup that I utilize to make new webapps and websites.
If there is anything that you think should be added/modified, feel free to make a pull request

Use at your own risk

## 🚀 GitHub Workflows (CI/CD)

This template includes comprehensive GitHub Actions workflows for automated testing, code quality checks, and dependency management. **Deployment is disabled by default** - perfect for template repositories.

### 📋 Available Workflows

#### 1. **Test and Deploy** (`test_and_deploy.yml`)
- **Purpose**: Main CI workflow that runs tests on every push and PR
- **Features**: 
  - Automated testing with PostgreSQL
  - Coverage reporting
  - Django system checks
  - Static file collection
- **Deployment**: Disabled by default (commented out)
- **Template Ready**: ✅ No secrets required

#### 2. **Code Quality** (`code-quality.yml`)
- **Purpose**: Linting, formatting, and type checking
- **Tools**: Ruff, Black, isort, Pylint, MyPy
- **Trigger**: On Python file changes
- **Template Ready**: ✅ No configuration needed

#### 3. **Dependabot Auto-Merge** (`dependabot-auto-merge.yml`)
- **Purpose**: Automated dependency updates with testing
- **Features**:
  - Auto-merge for minor/patch updates
  - Manual review for major updates
  - Security update prioritization
- **Template Ready**: ✅ Uses repository owner automatically
- **⚠️ Requires Labels**: Must set up repository labels (see setup instructions below)

#### 4. **Reusable Test Workflow** (`test-and-check.yml`)
- **Purpose**: Reusable testing workflow for other projects
- **Features**: Configurable Python/PostgreSQL versions
- **Template Ready**: ✅ Can be called by other workflows

### 🏷️ **Required Labels Setup**

The Dependabot auto-merge workflow requires specific repository labels to function properly. **This is the only manual setup required** after forking.

#### **Quick Setup (Recommended)**

```bash
# Make sure you have GitHub CLI installed and authenticated
chmod +x .github/scripts/setup-labels.sh
./github/scripts/setup-labels.sh
```

#### **Manual Setup**

If you prefer to set up labels manually, create these labels in your repository:

| Label | Color | Description |
|-------|-------|-------------|
| `auto-merge` | `#0E8A16` | Automatically merge when all checks pass |
| `security` | `#D93F0B` | Security-related updates and vulnerabilities |
| `dependencies` | `#0366D6` | Dependency updates and package management |
| `python` | `#3776AB` | Python-specific changes and updates |
| `github-actions` | `#2088FF` | GitHub Actions workflow changes |
| `docker` | `#2496ED` | Docker-related changes and updates |

#### **Why Labels Are Required**

- **`auto-merge`**: Dependabot PRs must have this label to be eligible for auto-merge
- **`security`**: Security updates get special handling and can auto-merge regardless of version type
- **`dependencies`**: Categorizes dependency-related PRs
- **Ecosystem labels**: Help organize and filter different types of updates

### 🔧 Configuration Required After Forking

#### **Dependabot Configuration**
The dependabot configuration automatically uses the repository owner, but you may want to customize:

```yaml
# .github/dependabot.yml
reviewers:
  - "your-username"  # Optional: override automatic detection
assignees:
  - "your-username"  # Optional: override automatic detection
```

#### **Optional Secrets** (for enhanced functionality)
```bash
# Only needed if you want to use external databases for testing
DATABASE_URL=postgres://user:pass@host:port/db

# Only needed if you enable deployment
NEW_CAPROVER_SERVER=your-server
CAPROVER_WEB_APP_NAME=your-app
NEW_CAPROVER_WEB_APP_TOKEN=your-token
PRODUCTION_URL=https://your-app.com
```

### 🚀 Enabling Deployment

To enable deployment after forking:

1. **Uncomment the deployment job** in `.github/workflows/test_and_deploy.yml`
2. **Configure required secrets** in your repository settings
3. **Update deployment configuration** for your hosting provider

```yaml
# Uncomment this section in test_and_deploy.yml
deploy-caprover:
  runs-on: ubuntu-latest
  # ... rest of deployment configuration
```

### 📊 Workflow Features

- **Concurrency Control**: Prevents workflow conflicts
- **Caching**: Optimized dependency and static file caching
- **Security**: Automated security audits with safety and pip-audit
- **Coverage**: Code coverage reporting with Codecov integration
- **Database**: PostgreSQL testing with health checks
- **Django**: Comprehensive Django-specific checks and testing

### 🔍 What Gets Tested

- ✅ Unit tests with coverage
- ✅ Database migrations
- ✅ Static file collection
- ✅ Django system checks
- ✅ Code formatting and linting
- ✅ Type checking
- ✅ Security vulnerabilities
- ✅ Dependency updates

### 📝 Template Benefits

- **Zero Configuration**: Works immediately after forking (except labels)
- **Production Ready**: Comprehensive testing without deployment
- **Customizable**: Easy to enable deployment when needed
- **Best Practices**: Follows GitHub Actions best practices
- **Reusable**: Can be adapted for other projects

---

**Note**: This template is designed to work out-of-the-box for new projects. All workflows are configured to run without requiring additional setup, making it perfect for rapid project initialization. **The only manual step required is setting up the repository labels for Dependabot auto-merge functionality.**
