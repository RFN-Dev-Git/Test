import subprocess
import os

def sync_work(token, repo_path, user_name, user_email):
    # 1. إعدادات الهوية
    os.system(f'git config --global user.email "{user_email}"')
    os.system(f'git config --global user.name "{user_name}"')

    # 2. التأكد من أن المجلد هو مستودع Git
    if not os.path.exists('.git'):
        subprocess.run(["git", "init"], check=True)
        print("Initialized Git repository.")

    # 3. بناء رابط الرفع بالـ Token
    # الرابط بيكون شكله كده: https://ghp_xxx@github.com/user/repo.git
    remote_url = f"https://{token}@github.com/{repo_path}.git"

    try:
        # إضافة الملفات
        subprocess.run(["git", "add", "."], check=True)
        
        # عمل Commit
        subprocess.run(["git", "commit", "-m", "Auto-sync from Arena AI"], check=True)

        # تحديد الفرع
        subprocess.run(["git", "branch", "-M", "main"], check=True)

        # الرفع (استخدام --force اختياري حسب رغبتك لضمان المزامنة)
        result = subprocess.run(["git", "push", remote_url, "main", "--force"], capture_output=True, text=True)
        
        if result.returncode == 0:
            return "✅ تم الرفع بنجاح! روح لـ VS Code واعمل git pull"
        else:
            return f"❌ فشل الرفع: {result.stderr}"
            
    except Exception as e:
        return f"⚠️ حدث خطأ تقني: {str(e)}"

# المهارة دي هتستنى منك البيانات عشان تشتغل
