import zipfile
import os

def zip_project(output_filename='my_project.zip'):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('.'):
            # تخطي المجلدات المخفية وملفات النظام
            if '.arena' in root or '.git' in root or '__pycache__' in root:
                continue
            for file in files:
                if file != output_filename: # لا تضغط ملف الزيب داخل نفسه
                    zipf.write(os.path.join(root, file))
    print(f"Done! Project packaged into {output_filename}")

if __name__ == "__main__":
    zip_project()
