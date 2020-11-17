i=1
factorial=1

n=int(input('Enter n:'))

while i<=n:
  factorial=factorial*i
  i=i+1

print(n, ' : ', factorial)