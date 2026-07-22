---
name: git-expert
description: >-
  Use this skill whenever the user wants to manage GitHub repositories, including 
  initializing a repo, creating branches, switching branches, pulling code, 
  or pushing changes with professional commit messages.
---

# Git Expert Skill

When triggered, follow this step-by-step process to manage the repository:

## 1. Environment Setup
* Check if `.git` directory exists.
* Ensure Git identity (email/name) is configured.
* Use the provided Personal Access Token (PAT) for all remote operations.

## 2. Execution Logic
* **Commits**: Analyze changes using `git diff` and generate a conventional commit message (feat, fix, docs, etc.).
* **Branches**: Create or switch branches as requested.
* **Sync**: Always attempt a `pull` before a `push` to avoid conflicts.

## 3. Safety Boundaries
* Never display the raw Token in the logs or `SKILL.md`.
* Ask for confirmation before performing a `--force` push.
* Validate repository URL format before connecting.

## 4. Helper Scripts
* Primary Logic: `scripts/logic.py`
