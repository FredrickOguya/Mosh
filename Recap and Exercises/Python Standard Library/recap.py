import zipfile

with zipfile.ZipFile('archive.zip') as zf:
    zf.extractall('extracted_folder')