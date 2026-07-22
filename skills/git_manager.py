import subprocess
import os

def git_push(repo_url, commit_message="Sync from Arena AI"):
    try:
        # التأكد من وجود Git
        if not os.path.exists('.git'):
            subprocess.run(["git", "init"], check=True)
            
        # إضافة كل الملفات
        subprocess.run(["git", "add", "."], check=True)
        
        # عمل Commit
        # ملاحظة: سنحتاج لضبط الـ user.email و user.name برمجياً قبل هذه الخطوة
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # تحديد الفرع الرئيسي
        subprocess.run(["git", "branch", "-M", "main"], check=True)
        
        # إضافة الـ Remote و الرفع
        # سنقوم بدمج الـ Token في الرابط بشكل آمن للرفع فقط
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main", "--force"], check=True)
        
        return "تم رفع الكود بنجاح!"
    except Exception as e:
        return f"حدث خطأ: {str(e)}"

# هذا السكربت سيتم تفعيله بمجرد إرسالك للبيانات
