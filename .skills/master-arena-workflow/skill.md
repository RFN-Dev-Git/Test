# ARENA AI PROJECT ACTIVATOR

Every skill or automated tool developed in this environment must be organized using the following directory format:
- Path: .skills/<foldername>/skill.md
- Each folder must contain a skill.md file defining the YAML frontmatter and logic for that specific task.

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

## 2. Project Discovery and Initialization
Before any file operations, the AI Agent MUST follow this safety sequence:
1. MANDATORY QUESTION: Ask the user: "Is this a new project or an existing one with files on GitHub?"
2. TECHNICAL VERIFICATION: Regardless of the answer, run "git ls-remote <repo-url>" to check if the repository is truly empty or contains existing branches/commits.
3. EXECUTION LOGIC:
   - IF EXISTING: Do NOT use "git init" and push. Instead, perform a "git clone" (or "git init + git remote add + git pull") to merge the remote code into the workspace.
   - IF NEW: Run "git init", set up the remote, and create the ".skills/" structure.
4. IDENTITY: Configure global "user.email" and "user.name" immediately after setup.
5. SYNC: Always run "git pull" before the first push to ensure no data loss.

## 3. Command Dictionary (Automated Actions)
Execute the following logic when these keywords are used:
- "push": Run "git add -A", analyze changes, generate a Conventional Commit message, and run "git push origin main".
- "pull": Check for local changes and run "git pull origin main".
- "sync": Execute a "pull" (resolve conflicts if any), then "add/commit", and finally "push".
- "status": Run "git status" and provide a human-readable summary of progress.

## 4. Code Guardian (Safety Protocol)
Before any push operation, the agent must:
1. Secret Scan: Search all staged files for strings like "ghp_" or API keys. ABORT if found.
2. Syntax Check: Run "python3 -m py_compile" on all .py files to ensure no breakage.
3. Audit: Warn if files larger than 5MB are being added.

## 5. Professional Git Standards
- Commits: Always use the "Conventional Commits" format (feat:, fix:, docs:, refactor:).
- Branches: Always confirm the target branch before destructive operations.
- Reporting: After every sync, output: Status | Commit Message | Next Step for User in VS Code.

---
ACTION REQUIRED:
Check the credentials above. If complete, initialize the environment. If anything is missing, ask the user now.
