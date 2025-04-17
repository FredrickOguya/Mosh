from pathlib import Path

path = Path()

#print(path.exists())
#print(path.mkdir())
#print(path.rmdir())
for file in path.glob('* '):
    print(file)