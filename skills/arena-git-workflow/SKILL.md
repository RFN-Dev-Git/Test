---
name: arena-git-workflow
description: >-
  Guide for managing coding projects with Arena AI and syncing them to a GitHub repository through VS Code. 
  Use this skill whenever the user wants to start a new project, initialize a Git repo, connect to a GitHub remote, 
  create or update files under a "skills" folder, or write a commit message for changes made in VS Code. 
  Trigger on phrases like "start a new project", "connect to my repo", "push this to GitHub", "init git", or "write a commit message".
---

# Arena AI + VS Code Git Workflow Guide

This is the reference guide for managing your coding projects with Arena AI and connecting them to a local VS Code environment through GitHub.

## Handling credentials

This workflow relies on a GitHub personal access token to authenticate pushes and pulls. Treat it as a secret:

- Never write the actual token value into this file, into committed code, or into any file that gets pushed to the repository.
- Store the token as an environment variable (e.g. `GITHUB_TOKEN`) or in a local, gitignored credentials file instead of pasting it into chat or into source files.
- If a token is ever pasted into a conversation or committed by mistake, revoke it on GitHub and generate a new one.

Fields to fill in for your own reference (keep this section untracked, e.g. in a local `.env` or `credentials.local.md` that is excluded via `.gitignore`):

- **GitHub Token:** *(store securely, do not commit)*
- **Repo URL:** `https://github.com/RFN-Dev-Git/Test.git`
- **User Info:** Arena AI Agent / agent@arena.ai

## Starting a new project in a new conversation

When opening a new conversation with Arena AI to work on a project, follow these steps:

1. Provide the repository URL (and, separately/securely, the token if the assistant needs to authenticate a push).
2. Ask the assistant to:
   > "Initialize Git (`git init`), connect it to the new repository using my token, create a `skills` folder, and start building the requested skill."

## Current folder structure

- `.arena/skills/` — organized skill directories (SKILL.md + scripts)
- `/skills` — legacy/automation scripts (maintained for compatibility)
- `/docs` — supplementary documentation

## Key VS Code commands

When the assistant pushes changes on your behalf, use these commands locally to stay in sync:

- `git clone [REPO_URL]` — download the project for the first time
- `git pull origin main` — pull the latest updates from the assistant
- `git add .` then `git commit -m "message"` then `git push` — send your local edits back to the repository

## Command dictionary — what each word means

| User says | What it means | What to do |
| :--- | :--- | :--- |
| **"push"** | Send changes to GitHub | `git add -A`, `git commit -m "<msg>"`, `git push origin <branch>` |
| **"pull"** | Get updates from GitHub | `git pull origin <branch>` (Warn if local conflicts exist) |
| **"commit"** | Save local snapshot | `git add -A` then `git commit -m "<msg>"` |
| **"init"** | Start Git tracking | `git init`, `git remote add origin <url>` |
| **"status"** | Show changes | `git status` and summarize in plain language |

## Tips for developing new skills

- Ask the assistant to create a "skill" for any repetitive task.
- Always use **Conventional Commits** (e.g., `feat:`, `fix:`, `docs:`) to keep history clean in VS Code.
