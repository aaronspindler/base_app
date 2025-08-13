#!/bin/bash

# Setup GitHub Labels Script
# This script creates all the labels needed for the dependabot auto-merge workflow
# Run this script from the root of your repository

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Setting up GitHub Labels for Dependabot Auto-Merge${NC}"
echo "=================================================="

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}❌ GitHub CLI (gh) is not installed.${NC}"
    echo "Please install it first: https://cli.github.com/"
    exit 1
fi

# Check if user is authenticated
if ! gh auth status &> /dev/null; then
    echo -e "${RED}❌ Not authenticated with GitHub CLI.${NC}"
    echo "Please run: gh auth login"
    exit 1
fi

# Get repository info
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
if [ -z "$REPO" ]; then
    echo -e "${RED}❌ Could not determine repository.${NC}"
    echo "Make sure you're in a git repository and have access to it."
    exit 1
fi

echo -e "${GREEN}✅ Repository: $REPO${NC}"

# Create labels from the labels.yml file
echo -e "${YELLOW}📝 Creating labels...${NC}"

# Check if labels.yml exists
if [ ! -f ".github/labels.yml" ]; then
    echo -e "${RED}❌ .github/labels.yml not found.${NC}"
    echo "Make sure you're running this script from the repository root."
    exit 1
fi

# Create labels using gh CLI
gh label create --repo "$REPO" --file .github/labels.yml

echo -e "${GREEN}✅ All labels created successfully!${NC}"
echo ""
echo -e "${BLUE}📋 Labels created:${NC}"
echo "  • auto-merge - Automatically merge when all checks pass"
echo "  • security - Security-related updates and vulnerabilities"
echo "  • dependencies - Dependency updates and package management"
echo "  • python - Python-specific changes and updates"
echo "  • github-actions - GitHub Actions workflow changes"
echo "  • docker - Docker-related changes and updates"
echo "  • Plus standard issue labels (bug, documentation, enhancement, etc.)"
echo ""
echo -e "${GREEN}🎉 Your repository is now ready for Dependabot auto-merge!${NC}"
echo ""
echo -e "${YELLOW}💡 Next steps:${NC}"
echo "  1. Push these changes to your repository"
echo "  2. Dependabot will automatically create PRs with the required labels"
echo "  3. The auto-merge workflow will handle minor and patch updates"
echo "  4. Major updates will require manual review"
echo ""
echo -e "${BLUE}📚 For more information, see the README.md file.${NC}"
