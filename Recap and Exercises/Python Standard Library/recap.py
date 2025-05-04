import zipfile

with zipfile.ZipFile("archive.zip") as zf:
    print(zf.namelist())