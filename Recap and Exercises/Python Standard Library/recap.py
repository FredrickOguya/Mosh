import zipfile

with zipfile.ZipFile('archive.zip', 'w') as zf:
    zf.write('projects/notes.txt')
    zf.write('projects/demo_project/README.md')