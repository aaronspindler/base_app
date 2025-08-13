# Contributing to Base App

First off, thank you for considering contributing to this Django template repository! 🎉

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Documentation](#documentation)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/base_app.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Push to your fork: `git push origin feature/your-feature-name`
6. Create a Pull Request

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, please include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment details (OS, Python version, Django version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Use cases for the enhancement
- Possible implementation approach (if you have ideas)

### Your First Code Contribution

Unsure where to begin? Look for issues labeled:
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `documentation` - Documentation improvements

## Development Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 15+ (or Docker for containerized development)
- Git

### Local Development

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   make install  # Or: pip install -r requirements.txt -r requirements-dev.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.template .env
   # Edit .env with your local settings
   ```

4. **Set up the database:**
   ```bash
   make migrate  # Or: python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   make superuser  # Or: python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   make run  # Or: python manage.py runserver
   ```

### Docker Development

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

2. **Run migrations in Docker:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

## Style Guidelines

### Python Style Guide

We use the following tools to maintain code quality:
- **Black** for code formatting (line length: 88)
- **isort** for import sorting
- **Ruff** for linting
- **MyPy** for type checking

Run all formatters and linters:
```bash
make format  # Format code
make lint    # Check code style
```

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality. Install them with:
```bash
pre-commit install
```

### Django Best Practices

- Use Django's built-in features when possible
- Follow Django's coding style
- Write descriptive model and field names
- Use Django's translation system for user-facing strings
- Keep views thin, move business logic to models or services
- Use Django's form validation

## Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements

### Examples:
```
feat(auth): add social authentication support
fix(api): handle null values in user serializer
docs: update installation instructions
```

## Pull Request Process

1. **Update your branch:**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests:**
   ```bash
   make test  # Or: pytest
   ```

3. **Update documentation** if needed

4. **Ensure all checks pass:**
   ```bash
   make ci  # Runs linting, tests, and deployment checks
   ```

5. **Create Pull Request:**
   - Use a clear, descriptive title
   - Reference any related issues
   - Describe what changes were made and why
   - Include screenshots for UI changes

6. **Code Review:**
   - Address reviewer feedback
   - Keep discussions focused and professional
   - Update your PR based on feedback

## Testing

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-coverage

# Run specific test file
pytest tests/test_views.py

# Run tests in parallel
make test-fast
```

### Writing Tests

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern
- Use fixtures for common test data

Example test:
```python
@pytest.mark.django_db
def test_user_creation(client):
    """Test that a user can be created successfully."""
    # Arrange
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'securepass123'
    }
    
    # Act
    response = client.post('/api/users/', user_data)
    
    # Assert
    assert response.status_code == 201
    assert response.data['email'] == user_data['email']
```

## Documentation

- Update the README.md if you change functionality
- Add docstrings to all functions and classes
- Update type hints where applicable
- Include examples in docstrings when helpful
- Keep documentation up-to-date with code changes

### Docstring Example:
```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the discounted price.
    
    Args:
        price: The original price
        discount_percent: The discount percentage (0-100)
    
    Returns:
        The discounted price
    
    Example:
        >>> calculate_discount(100, 20)
        80.0
    """
    return price * (1 - discount_percent / 100)
```

## Questions?

Feel free to open an issue with the label `question` or start a discussion in the GitHub Discussions section.

Thank you for contributing! 🚀
