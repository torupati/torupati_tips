from pathlib import Path

p = Path(__file__).parent
print('p.iterdir()')
for child in p.iterdir():
    print(child)
print('')
print('glob("**/*.py")')
for f in p.glob("**/*.py"):
    print(f)
print('')
print('glob("**/*")')
for f in p.glob("**/*"):
    print(f)


