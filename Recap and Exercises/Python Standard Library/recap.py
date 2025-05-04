# 💻 Your Practice Task
# ✅ Write a script that:
# 1️⃣ Creates a zip file called demo_project.zip
# 2️⃣ Adds both projects/notes.txt and projects/demo_project/README.md
# 3️⃣ Lists the contents of the zip
# 4️⃣ Extracts the zip to a folder called unzipped_demo

import zipfile

with zipfile.ZipFile('demo_project.zip','w') as zf:
    zf.write('projects/notes.txt')
    zf.write('projects/demo_project/README.md')

with zipfile.ZipFile('demo_project.zip') as rf:
    print(rf.namelist())

with zipfile.Zipfile('demo_project.zip') as ef:
    ef.extratractall('unzipped_demo')