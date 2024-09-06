n: int = 1_000_000_000
print(n)

n: int = 1000000000
print(f'{n:_}')
print(f'{n:,}')

var: str = 'var'
print(f'{var:>20}')
print(f'{var:<20}')
print(f'{var:20}')
print(f'{var:^20}')

print(f'{var:_>20}')
print(f'{var:|<20}')
print(f'{var:20}')
print(f'{var:&^20}')

from datetime import datetime
now: datetime = datetime.now()
print(f'{now:%d.%m.%y}')
print(f'{now:%c}')
print(f'{now:%H:%M:%S}')
print(f'{now:%I%p}')

n: float = 1234.5678
print(n)
print(round(n,2))
print(f'{n:.2f}')
print(f'{n:.2}')
print(f'{n:,.3f}')

a: int = 5
b: int = 10
my_var: str = "bob says hi"

print(f'a + b = {a+b}')
print(f'{a + b = }')
print(f'{bool(a) = }')