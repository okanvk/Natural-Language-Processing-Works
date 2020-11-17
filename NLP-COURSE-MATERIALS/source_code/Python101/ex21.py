sum_of_divisors=0
i=1

n=int(input('Enter a number:'))

while i<=(n//2):
  if n%i==0:
    sum_of_divisors=sum_of_divisors+i
  i=i+1

if n==sum_of_divisors:
  print(n,'is a perfect number')
else:
  print(n,'is not a perfect number')