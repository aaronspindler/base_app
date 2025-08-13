# Setup GitHub Labels Script for Windows
# This script creates all the labels needed for the dependabot auto-merge workflow
# Run this script from the root of your repository

param(
    [string]$Repo = ""
)

# Colors for output
$Red = "Red"
$Green = "Green"
$Yellow = "Yellow"
$Blue = "Blue"

Write-Host "🚀 Setting up GitHub Labels for Dependabot Auto-Merge" -ForegroundColor $Blue
Write-Host "==================================================" -ForegroundColor $Blue

# Check if gh CLI is installed
try {
    $null = Get-Command gh -ErrorAction Stop
} catch {
    Write-Host "❌ GitHub CLI (gh) is not installed." -ForegroundColor $Red
    Write-Host "Please install it first: https://cli.github.com/" -ForegroundColor $Red
    exit 1
}

# Check if user is authenticated
try {
    $null = gh auth status 2>$null
} catch {
    Write-Host "❌ Not authenticated with GitHub CLI." -ForegroundColor $Red
    Write-Host "Please run: gh auth login" -ForegroundColor $Red
    exit 1
}

# Get repository info
if ($Repo -eq "") {
    try {
        $Repo = gh repo view --json nameWithOwner -q .nameWithOwner
    } catch {
        Write-Host "❌ Could not determine repository." -ForegroundColor $Red
        Write-Host "Make sure you're in a git repository and have access to it." -ForegroundColor $Red
        Write-Host "Or specify the repository with: -Repo owner/repo" -ForegroundColor $Red
        exit 1
    }
}

if ($Repo -eq "") {
    Write-Host "❌ Could not determine repository." -ForegroundColor $Red
    Write-Host "Make sure you're in a git repository and have access to it." -ForegroundColor $Red
    exit 1
}

Write-Host "✅ Repository: $Repo" -ForegroundColor $Green

# Create labels from the labels.yml file
Write-Host "📝 Creating labels..." -ForegroundColor $Yellow

# Check if labels.yml exists
if (-not (Test-Path ".github/labels.yml")) {
    Write-Host "❌ .github/labels.yml not found." -ForegroundColor $Red
    Write-Host "Make sure you're running this script from the repository root." -ForegroundColor $Red
    exit 1
}

# Create labels using gh CLI
try {
    gh label create --repo "$Repo" --file .github/labels.yml
} catch {
    Write-Host "❌ Error creating labels. Please check your permissions and try again." -ForegroundColor $Red
    exit 1
}

Write-Host "✅ All labels created successfully!" -ForegroundColor $Green
Write-Host ""
Write-Host "📋 Labels created:" -ForegroundColor $Blue
Write-Host "  • auto-merge - Automatically merge when all checks pass" -ForegroundColor $Green
Write-Host "  • security - Security-related updates and vulnerabilities" -ForegroundColor $Green
Write-Host "  • dependencies - Dependency updates and package management" -ForegroundColor $Green
Write-Host "  • python - Python-specific changes and updates" -ForegroundColor $Green
Write-Host "  • github-actions - GitHub Actions workflow changes" -ForegroundColor $Green
Write-Host "  • docker - Docker-related changes and updates" -ForegroundColor $Green
Write-Host "  • Plus standard issue labels (bug, documentation, enhancement, etc.)" -ForegroundColor $Green
Write-Host ""
Write-Host "🎉 Your repository is now ready for Dependabot auto-merge!" -ForegroundColor $Green
Write-Host ""
Write-Host "💡 Next steps:" -ForegroundColor $Yellow
Write-Host "  1. Push these changes to your repository" -ForegroundColor $Yellow
Write-Host "  2. Dependabot will automatically create PRs with the required labels" -ForegroundColor $Yellow
Write-Host "  3. The auto-merge workflow will handle minor and patch updates" -ForegroundColor $Yellow
Write-Host "  4. Major updates will require manual review" -ForegroundColor $Yellow
Write-Host ""
Write-Host "📚 For more information, see the README.md file." -ForegroundColor $Blue
