# ARENA AI PROJECT ACTIVATOR

Use the following standardized Skill specification to initialize the development environment and manage the synchronization with GitHub and VS Code.

---
name: master-arena-workflow
description: >-
  A comprehensive skill for project initialization, professional Git management, 
  and safety-first coding workflows. Use this to sync Arena AI with VS Code via GitHub.
---

# Master Workspace Instructions

## 1. Credentials and Identity Verification
Before proceeding with any initialization, check if the following values are provided. If they are missing, empty, or still contain placeholders (e.g., [INSERT_...]), you MUST explicitly ask the user to provide them:
- GitHub Token: [INSERT_YOUR_TOKEN_HERE]
- Repository URL: [INSERT_REPO_URL_HERE]
- User Info: [INSERT_NAME] / [INSERT_EMAIL]

## 2. Skill Directory Structure
Every skill or automated tool must be organized using the following directory format:
- Path: .skills/<foldername>/skill.md
- Each folder must contain a skill.md file defining the YAML frontmatter and logic for that specific task.

## 3. Initialization Protocol
Once credentials are confirmed, the AI Agent must immediately:
1. Run "git init" in the workspace root.
2. Configure global "user.email" and "user.name" using the User Info provided.
3. Connect to the remote repository using the provided Token.
4. Create the ".skills/" base directory.
5. Create a default skill folder: ".skills/git-workflow/skill.md" and save these instructions there.
6. Perform an initial push to verify the connection.

## 4. Command Dictionary (Automated Actions)
Execute the following logic when these keywords are used:
- "push": Run "git add -A", analyze changes, generate a Conventional Commit message, and run "git push origin main".
- "pull": Check for local changes and run "git pull origin main".
- "sync": Execute a "pull" (resolve conflicts if any), then "add/commit", and finally "push".
- "status": Run "git status" and provide a human-readable summary of progress.

## 5. Code Guardian (Safety Protocol)
Before any push operation, the agent must:
1. Secret Scan: Search all staged files for strings like "ghp_" or API keys. ABORT if found.
2. Syntax Check: Run "python3 -m py_compile" on all .py files to ensure no breakage.
3. Audit: Warn if files larger than 5MB are being added.

## 6. Professional Git Standards
- Commits: Always use the "Conventional Commits" format (feat:, fix:, docs:, refactor:).
- Branches: Always confirm the target branch before destructive operations.
- Reporting: After every sync, output: Status | Commit Message | Next Step for User in VS Code.

---
ACTION REQUIRED:
Check the credentials above. If complete, initialize the environment. If anything is missing, ask the user now.
