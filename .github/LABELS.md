# GitHub Labels Required for Dependabot Auto-Merge

This document explains the labels required for the Dependabot auto-merge workflow to function properly.

## 🏷️ Required Labels

### **Core Labels (Required for Auto-Merge)**

| Label | Color | Description | Required For |
|-------|-------|-------------|--------------|
| `auto-merge` | `#0E8A16` | Automatically merge when all checks pass | **All auto-merge functionality** |
| `security` | `#D93F0B` | Security-related updates and vulnerabilities | **Security update auto-merge** |

### **Category Labels (Used for Organization)**

| Label | Color | Description | Purpose |
|-------|-------|-------------|---------|
| `dependencies` | `#0366D6` | Dependency updates and package management | Categorize dependency PRs |
| `python` | `#3776AB` | Python-specific changes and updates | Python ecosystem updates |
| `github-actions` | `#2088FF` | GitHub Actions workflow changes | Actions updates |
| `docker` | `#2496ED` | Docker-related changes and updates | Docker updates |

### **Standard Issue Labels (Optional but Recommended)**

| Label | Color | Description |
|-------|-------|-------------|
| `bug` | `#D73A4A` | Something isn't working |
| `documentation` | `#0075CA` | Improvements or additions to documentation |
| `enhancement` | `#A2EEEF` | New feature or request |
| `good first issue` | `#7057FF` | Good for newcomers |
| `help wanted` | `#008672` | Extra attention is needed |
| `invalid` | `#E4E669` | Something is wrong |
| `question` | `#CC317C` | Further information is requested |
| `wontfix` | `#FFFFFF` | This will not be worked on |

## 🚀 Quick Setup

### **Option 1: Automated Setup (Recommended)**

```bash
# Make sure you have GitHub CLI installed and authenticated
chmod +x .github/scripts/setup-labels.sh
./github/scripts/setup-labels.sh
```

### **Option 2: Manual Setup**

1. Go to your repository on GitHub
2. Click on "Issues" → "Labels"
3. Click "New label" for each required label
4. Use the colors and descriptions from the table above

### **Option 3: Windows PowerShell**

```powershell
# Run the PowerShell script
.\.github\scripts\setup-labels.ps1
```

## 🔍 How Labels Work

### **Auto-Merge Logic**

1. **Dependabot creates PR** with appropriate labels
2. **Workflow checks for `auto-merge` label** - this is the main requirement
3. **Tests run automatically** on the PR
4. **If tests pass and `auto-merge` label exists**:
   - Minor/patch updates: Auto-merge enabled
   - Major updates: Comment added, manual review required
   - Security updates: Auto-merge enabled regardless of version

### **Label Assignment**

- **Dependabot automatically assigns** the required labels based on `.github/dependabot.yml`
- **`auto-merge` label** is added to all dependency updates
- **`security` label** is added to security-related updates
- **Ecosystem labels** are added based on the package type

## ⚠️ Common Issues

### **Auto-Merge Not Working?**

1. **Check if `auto-merge` label exists** in your repository
2. **Verify Dependabot is configured** in `.github/dependabot.yml`
3. **Ensure tests are passing** - auto-merge only works on successful test runs
4. **Check repository permissions** - Dependabot needs write access

### **Labels Not Being Applied?**

1. **Verify Dependabot configuration** is correct
2. **Check if Dependabot is enabled** for your repository
3. **Ensure the repository has the required labels** created
4. **Wait for the next Dependabot run** (runs daily by default)

## 📚 Additional Resources

- [GitHub Labels Documentation](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)
- [Dependabot Configuration](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file)
- [GitHub CLI Installation](https://cli.github.com/)

## 🎯 Summary

**The only manual setup required** after forking this template is creating the repository labels. Once labels are set up:

- ✅ Dependabot will automatically create PRs with proper labels
- ✅ Auto-merge will work for minor/patch updates
- ✅ Security updates will be prioritized
- ✅ Major updates will require manual review
- ✅ All testing and quality checks run automatically

This ensures your repository gets the benefits of automated dependency management with proper safety controls.
