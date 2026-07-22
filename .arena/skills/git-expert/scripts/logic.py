import subprocess
import os

class GitExpert:
    def __init__(self, token=None, repo_url=None, user_name=None, user_email=None):
        self.token = token
        self.repo_url = repo_url # example: github.com/user/repo
        self.user_name = user_name
        self.user_email = user_email
        
        if user_name and user_email:
            self._run_cmd(f'git config --global user.email "{user_email}"')
            self._run_cmd(f'git config --global user.name "{user_name}"')

    def _run_cmd(self, cmd):
        try:
            # دمج التوكن في الأمر إذا كان متاحاً
            if self.token and "github.com" in cmd and "https://" in cmd:
                cmd = cmd.replace("https://", f"https://{self.token}@")
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
        except Exception as e:
            return str(e)

    def status(self):
        return self._run_cmd("git status")

    def create_branch(self, branch_name):
        return self._run_cmd(f"git checkout -b {branch_name}")

    def switch_branch(self, branch_name):
        return self._run_cmd(f"git checkout {branch_name}")

    def commit(self, message):
        self._run_cmd("git add .")
        return self._run_cmd(f'git commit -m "{message}"')

    def push(self, branch="main"):
        remote_url = f"https://{self.token}@github.com/{self.repo_url}.git"
        return self._run_cmd(f"git push {remote_url} {branch} --force")

    def pull(self, branch="main"):
        remote_url = f"https://{self.token}@github.com/{self.repo_url}.git"
        return self._run_cmd(f"git pull {remote_url} {branch}")

# سيتم استدعاء هذا الكلاس بواسطة المساعد (أنا) لتنفيذ طلباتك
