from pathlib import Path

base = Path('projects/demo_project')
base.mkdir(parents=True,exist_ok=True)

notes = base/'notes.txt'
notes.write_text("This is a note")

readme = base / 'readme.md'
readme.write_text("#Demo Project")

for items in base.iterdir():
    print(items.resolve())

readme.rename(base / 'README.md')
notes.rename(base.parent / 'notes.txt')