from pathlib import Path

p = Path(__file__).parent
print('p=', p, ' type(p)=', type(p))
print('p.name=', p.name)
print('p.is_dir=', p.is_dir(), ' p.is_file=', p.is_file())
print('---')

p2 = p/Path('hoge')/Path('foo')
p2 = Path('hoge','foo')
print('p2=', str(p2))
print('p2.name=', p2.name)
print('p2.parts=', p2.parts)
print('p2.exsits=', p2.exists())

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


