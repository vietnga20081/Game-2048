# 2048 Game Makefile

# Variables
PYTHON = python3
PIP = pip3
VENV = venv
PROJECT_NAME = 2048-game
DOCKER_IMAGE = $(PROJECT_NAME):latest

# Colors for output
BLUE = \033[0;34m
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

.PHONY: help install dev-install run clean test lint format build-exe build-android build-docker run-docker setup-venv activate

# Default target
help: ## Show this help message
	@echo "$(BLUE)2048 Game - Makefile Help$(NC)"
	@echo "================================"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "$(GREEN)%-20s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Development setup
setup-venv: ## Create virtual environment
	@echo "$(YELLOW)Creating virtual environment...$(NC)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)Virtual environment created!$(NC)"
	@echo "Activate it with: source $(VENV)/bin/activate (Linux/Mac) or $(VENV)\\Scripts\\activate (Windows)"

install: ## Install dependencies
	@echo "$(YELLOW)Installing dependencies...$(NC)"
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)Dependencies installed!$(NC)"

dev-install: ## Install development dependencies
	@echo "$(YELLOW)Installing development dependencies...$(NC)"
	$(PIP) install -r requirements.txt
	$(PIP) install pytest pytest-cov black flake8 isort pyinstaller buildozer
	@echo "$(GREEN)Development dependencies installed!$(NC)"

# Running the game
run: ## Run the game (Pygame version)
	@echo "$(YELLOW)Starting 2048 Game (Pygame)...$(NC)"
	$(PYTHON) main.py

run-mobile: ## Run the mobile version (Kivy)
	@echo "$(YELLOW)Starting 2048 Game (Kivy Mobile)...$(NC)"
	$(PYTHON) kivy_main.py

# Code quality
test: ## Run tests
	@echo "$(YELLOW)Running tests...$(NC)"
	$(PYTHON) -m pytest tests/ -v --cov=. --cov-report=html
	@echo "$(GREEN)Tests completed!$(NC)"

lint: ## Run linting
	@echo "$(YELLOW)Running linter...$(NC)"
	flake8 *.py
	@echo "$(GREEN)Linting completed!$(NC)"

format: ## Format code
	@echo "$(YELLOW)Formatting code...$(NC)"
	black *.py
	isort *.py
	@echo "$(GREEN)Code formatted!$(NC)"

# Building executables
build-exe: ## Build executable for current platform
	@echo "$(YELLOW)Building executable...$(NC)"
	pyinstaller --onefile --windowed --name "$(PROJECT_NAME)" --add-data "*.json:." main.py
	@echo "$(GREEN)Executable
