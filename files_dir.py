from pathlib import Path

path = Path()
for file in path.glob('_Project/*.py'):
    print(file)

# path = Path("ecommerce")
# print(path.exists())
# print(path.mkdir())
# print(path.rmdir())