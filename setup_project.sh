#!/bin/bash

# 🎮 2048 Game Project Setup Script
# This script automates the entire project setup process

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_NAME="2048-game"
GITHUB_USERNAME=""  # Will be prompted

echo -e "${BLUE}🎮 2048 Game Project Setup${NC}"
echo "=================================="

# Function to print colored output
print_step() {
    echo -e "${GREEN}[STEP]${NC} $1"
}

print_info() {
    echo -e "${YELLOW}[INFO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if git is installed
check_git() {
    if ! command -v git &> /dev/null; then
        print_error "Git is not installed. Please install Git first."
        exit 1
    fi
}

# Check if Python is installed
check_python() {
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3 first."
        exit 1
    fi
}

# Get GitHub username
get_github_username() {
    echo -e "${YELLOW}Please enter your GitHub username:${NC}"
    read -r GITHUB_USERNAME
    
    if [ -z "$GITHUB_USERNAME" ]; then
        print_error "GitHub username cannot be empty!"
        exit 1
    fi
}

# Create project directory
create_project_dir() {
    print_step "Creating project directory..."
    
    if [ -d "$PROJECT_NAME" ]; then
        print_info "Directory $PROJECT_NAME already exists. Removing..."
        rm -rf "$PROJECT_NAME"
    fi
    
    mkdir "$PROJECT_NAME"
    cd "$PROJECT_NAME"
    
    print_info "Created directory: $PROJECT_NAME"
}

# Create directory structure
create_directory_structure() {
    print_step "Creating directory structure..."
    
    mkdir -p .github/workflows
    mkdir -p tests
    mkdir -p docs
    
    print_info "Directory structure created!"
}

# Create .gitignore file
create_gitignore() {
    print_step "Creating .gitignore file..."
    
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Game saves
best_score.json
saves/

# Build artifacts
*.spec
bin/
.buildozer/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
EOF

    print_info ".gitignore created!"
}

# Create main Python files (placeholder - user should copy the actual files)
create_python_files() {
    print_step "Creating Python files..."
    
    # Create placeholder main.py
    cat > main.py << 'EOF'
# TODO: Copy the actual main.py content from the artifact
# This is a placeholder file
print("2048 Game - Please copy the actual main.py content")
EOF

    # Create placeholder kivy_main.py
    cat > kivy_main.py << 'EOF'
# TODO: Copy the actual kivy_main.py content from the artifact
# This is a placeholder file
print("2048 Game Mobile - Please copy the actual kivy_main.py content")
EOF

    print_info "Python files created (placeholders)!"
}

# Create requirements.txt
create_requirements() {
    print_step "Creating requirements.txt..."
    
    cat > requirements.txt << 'EOF'
pygame==2.5.2
kivy==2.2.0
kivymd==1.1.1
EOF

    print_info "requirements.txt created!"
}

# Create GitHub Actions workflow
create_github_actions() {
    print_step "Creating GitHub Actions workflow..."
    
    # The workflow content is too long, so we'll create a placeholder
    cat > .github/workflows/build.yml << 'EOF'
# TODO: Copy the actual GitHub Actions workflow from the artifact
# This will handle building for Windows, macOS, Linux, and Android
name: Build Multi-Platform 2048 Game

on:
  push:
    branches: [ main, develop ]
    tags: [ 'v*' ]
  pull_request:
    branches: [ main ]

# Add the full workflow content here
EOF

    print_info "GitHub Actions workflow created!"
}

# Initialize git repository
init_git() {
    print_step "Initializing Git repository..."
    
    git init
    git add .
    git commit -m "Initial commit: 2048 game with multi-platform support"
    
    print_info "Git repository initialized!"
}

# Create GitHub repository (requires GitHub CLI)
create_github_repo() {
    print_step "Creating GitHub repository..."
    
    if command -v gh &> /dev/null; then
        gh repo create "$PROJECT_NAME" --public --description "2048 puzzle game with multi-platform support"
        git remote add origin "https://github.com/$GITHUB_USERNAME/$PROJECT_NAME.git"
        git branch -M main
        git push -u origin main
        
        print_info "GitHub repository created and code pushed!"
    else
        print_info "GitHub CLI not found. You'll need to create the repository manually."
        print_info "1. Go to https://github.com/new"
        print_info "2. Create repository named: $PROJECT_NAME"
        print_info "3. Run these commands:"
        echo "   git remote add origin https://github.com/$GITHUB_USERNAME/$PROJECT_NAME.git"
        echo "   git branch -M main"
        echo "   git push -u origin main"
    fi
}

# Setup virtual environment
setup_venv() {
    print_step "Setting up virtual environment..."
    
    python3 -m venv venv
    
    print_info "Virtual environment created!"
    print_info "Activate it with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"
}

# Create setup instructions
create_setup_instructions() {
    print_step "Creating setup instructions..."
    
    cat > SETUP_INSTRUCTIONS.md << EOF
# 🚀 Setup Instructions

## Files you need to copy from the artifacts:

1. **main.py** - Copy the full pygame version
2. **kivy_main.py** - Copy the full kivy mobile version  
3. **setup.py** - Copy the setup configuration
4. **pyproject.toml** - Copy the project configuration
5. **buildozer.spec** - Copy the Android build config
6. **.github/workflows/build.yml** - Copy the full GitHub Actions workflow
7. **Dockerfile** - Copy the Docker configuration
8. **docker-compose.yml** - Copy the Docker Compose config
9. **Makefile** - Copy the build automation
10. **README.md** - Copy the full documentation

## Next steps:

1. **Copy all artifact files** to replace the placeholders
2. **Activate virtual environment**: \`source venv/bin/activate\`
3. **Install dependencies**: \`pip install -r requirements.txt\`
4. **Test the game**: \`python main.py\`
5. **Push to GitHub**: If not done automatically
6. **Create a release**: \`git tag v1.0.0 && git push origin v1.0.0\`

## GitHub repository:
https://github.com/$GITHUB_USERNAME/$PROJECT_NAME

## Build status will be available at:
https://github.com/$GITHUB_USERNAME/$PROJECT_NAME/actions

Happy coding! 🎮
EOF

    print_info "Setup instructions created!"
}

# Main execution
main() {
    check_git
    check_python
    get_github_username
    
    create_project_dir
    create_directory_structure
    create_gitignore
    create_python_files
    create_requirements
    create_github_actions
    create_setup_instructions
    
    init_git
    setup_venv
    create_github_repo
    
    echo ""
    echo -e "${GREEN}✅ Project setup completed!${NC}"
    echo ""
    echo -e "${YELLOW}📁 Project location:${NC} $(pwd)"
    echo -e "${YELLOW}🔗 GitHub repository:${NC} https://github.com/$GITHUB_USERNAME/$PROJECT_NAME"
    echo ""
    echo -e "${BLUE}📋 Next steps:${NC}"
    echo "1. Copy all the artifact files to replace placeholders"
    echo "2. Activate virtual environment: source venv/bin/activate"
    echo "3. Install dependencies: pip install -r requirements.txt"
    echo "4. Test the game: python main.py"
    echo "5. Read SETUP_INSTRUCTIONS.md for detailed steps"
    echo ""
    echo -e "${GREEN}Happy coding! 🎮${NC}"
}

# Run main function
main
