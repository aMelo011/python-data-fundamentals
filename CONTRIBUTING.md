# Contributing Guidelines

Thank you for your interest in contributing to the Python Data Fundamentals ETL pipeline. This document outlines the standard procedures for contributing to this repository to maintain code quality and a clean Git history.

## Branching Strategy

We follow a simplified feature-branch workflow. 

1. Main Branch: `main` is locked and reflects the production-ready state.
2. Feature Branches: Create a new branch for every feature or bug fix.
   - Naming convention: `type/issue-description`
   - Examples: `feat/add-postgres-support`, `fix/api-timeout`, `docs/update-readme`

## Commit Message Convention

This project strictly adheres to [Conventional Commits](https://www.conventionalcommits.org/). This allows for automated changelog generation and clear versioning.

Format: `type(optional-scope): description`

Allowed Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

Example: `feat(database): migrate from sqlite to postgresql`

## Local Development Setup

To ensure your code integrates smoothly, please follow these steps before submitting a Pull Request:

1. Sync with the main branch.
2. Ensure your virtual environment (`.venv`) is active.
3. Install all requirements: `pip install -r requirements.txt`
4. Run the orchestrator locally to verify the pipeline executes without errors:
   `python3 main.py`

## Pull Request Process

1. Push your feature branch to the remote repository.
2. Open a Pull Request against the `main` branch.
3. Provide a clear description of the problem solved or the feature added.
4. Wait for code review before merging.
