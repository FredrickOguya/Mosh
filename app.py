from pathlib import Path

# Path("/fredrick/videos")
path = Path("ecommerce/__init__.py")
# Path() /"ecommerce" / "__init__.py"
# Path.home()

path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_suffix(".txt")
print(path.absolute())
