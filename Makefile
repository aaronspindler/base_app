# Makefile for Django Project
# Run 'make help' to see available commands

.PHONY: help
help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ==================== Setup Commands ====================

.PHONY: install
install: ## Install all dependencies (production + development)
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

.PHONY: install-prod
install-prod: ## Install production dependencies only
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: setup
setup: install migrate collectstatic ## Complete initial setup

.PHONY: venv
venv: ## Create virtual environment
	python3 -m venv venv
	@echo "Virtual environment created. Activate with: source venv/bin/activate"

.PHONY: update-deps
update-deps: ## Update all dependencies to latest versions
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	pip install --upgrade -r requirements-dev.txt
	pip freeze > requirements-lock.txt

# ==================== Database Commands ====================

.PHONY: migrate
migrate: ## Run database migrations
	python manage.py migrate

.PHONY: makemigrations
makemigrations: ## Create new migrations
	python manage.py makemigrations

.PHONY: migrations-check
migrations-check: ## Check for missing migrations
	python manage.py makemigrations --check --dry-run

.PHONY: db-reset
db-reset: ## Reset database (drops and recreates)
	python manage.py reset_db --noinput
	python manage.py migrate
	@echo "Database reset complete. You may want to run 'make superuser' to create an admin user."

.PHONY: superuser
superuser: ## Create a superuser
	python manage.py createsuperuser

.PHONY: shell
shell: ## Open Django shell (with shell_plus if available)
	@if python manage.py help shell_plus > /dev/null 2>&1; then \
		python manage.py shell_plus --ipython; \
	else \
		python manage.py shell; \
	fi

.PHONY: dbshell
dbshell: ## Open database shell
	python manage.py dbshell

# ==================== Development Commands ====================

.PHONY: run
run: ## Run development server
	python manage.py runserver

.PHONY: run-plus
run-plus: ## Run development server with Werkzeug debugger (requires django-extensions)
	python manage.py runserver_plus --cert-file cert.crt

.PHONY: collectstatic
collectstatic: ## Collect static files
	python manage.py collectstatic --noinput

.PHONY: clean
clean: ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".coverage" -delete
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf staticfiles/
	rm -rf media/
	rm -rf dist/
	rm -rf *.egg-info

# ==================== Testing Commands ====================

.PHONY: test
test: ## Run all tests
	pytest -v

.PHONY: test-coverage
test-coverage: ## Run tests with coverage report
	pytest --cov=. --cov-report=html --cov-report=term-missing

.PHONY: test-fast
test-fast: ## Run tests in parallel
	pytest -n auto

.PHONY: test-unit
test-unit: ## Run unit tests only
	pytest -m unit

.PHONY: test-integration
test-integration: ## Run integration tests only
	pytest -m integration

.PHONY: test-failed
test-failed: ## Re-run only failed tests
	pytest --lf

.PHONY: coverage-html
coverage-html: ## Generate HTML coverage report
	coverage html
	@echo "Coverage report generated. Open htmlcov/index.html to view."

# ==================== Code Quality Commands ====================

.PHONY: lint
lint: ## Run all linters
	ruff check .
	black --check .
	isort --check-only .
	mypy .

.PHONY: format
format: ## Format code with black and isort
	black .
	isort .
	ruff check --fix .

.PHONY: ruff
ruff: ## Run ruff linter
	ruff check .

.PHONY: ruff-fix
ruff-fix: ## Run ruff with auto-fix
	ruff check --fix .

.PHONY: black
black: ## Format code with black
	black .

.PHONY: isort
isort: ## Sort imports with isort
	isort .

.PHONY: mypy
mypy: ## Run type checking with mypy
	mypy .

.PHONY: security
security: ## Run security checks
	bandit -r . -ll
	safety check
	pip-audit

.PHONY: pre-commit
pre-commit: ## Run pre-commit hooks on all files
	pre-commit run --all-files

.PHONY: pre-commit-update
pre-commit-update: ## Update pre-commit hooks
	pre-commit autoupdate

# ==================== Docker Commands ====================

.PHONY: docker-build
docker-build: ## Build Docker image
	docker-compose build

.PHONY: docker-up
docker-up: ## Start Docker containers
	docker-compose up -d

.PHONY: docker-down
docker-down: ## Stop Docker containers
	docker-compose down

.PHONY: docker-logs
docker-logs: ## View Docker logs
	docker-compose logs -f

.PHONY: docker-shell
docker-shell: ## Open shell in web container
	docker-compose exec web bash

.PHONY: docker-clean
docker-clean: ## Clean Docker resources
	docker-compose down -v
	docker system prune -f

.PHONY: docker-rebuild
docker-rebuild: docker-down docker-build docker-up ## Rebuild and restart containers

# ==================== Documentation Commands ====================

.PHONY: docs
docs: ## Generate documentation
	@echo "Documentation generation not configured yet"

.PHONY: check-readme
check-readme: ## Check README for issues
	@echo "Checking README.md..."
	@test -f README.md || echo "WARNING: README.md not found"

# ==================== Deployment Commands ====================

.PHONY: deploy-check
deploy-check: ## Check deployment readiness
	python manage.py check --deploy
	python manage.py makemigrations --check --dry-run
	@echo "Deployment checks passed!"

.PHONY: prod-requirements
prod-requirements: ## Generate production requirements
	pip-compile requirements.in -o requirements.txt

# ==================== Utility Commands ====================

.PHONY: urls
urls: ## Show all URL patterns
	python manage.py show_urls

.PHONY: admin
admin: ## Open Django admin in browser
	@echo "Opening Django admin at http://localhost:8000/admin/"
	@python -m webbrowser http://localhost:8000/admin/

.PHONY: graph-models
graph-models: ## Generate model graph (requires django-extensions and graphviz)
	python manage.py graph_models -a -o models.png

.PHONY: validate-templates
validate-templates: ## Validate Django templates
	python manage.py validate_templates

.PHONY: find-todos
find-todos: ## Find all TODO comments in code
	@grep -r "TODO\|FIXME\|HACK\|NOTE" --include="*.py" --include="*.html" --include="*.js" --include="*.css" . || echo "No TODOs found"

.PHONY: check-migrations
check-migrations: ## List all migrations and their status
	python manage.py showmigrations

# ==================== CI/CD Commands ====================

.PHONY: ci
ci: lint test deploy-check ## Run all CI checks

.PHONY: github-setup
github-setup: ## Setup GitHub labels for workflows
	chmod +x .github/scripts/setup-labels.sh
	./.github/scripts/setup-labels.sh

# Default target
.DEFAULT_GOAL := help
