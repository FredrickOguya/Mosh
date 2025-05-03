from pathlib import Path

folder = Path('Demo_folder')
folder.mkdir(exist_ok=True)

file = folder / 'test.txt'
file.write_text('Holla')

file.unlink()
folder.rmdir()