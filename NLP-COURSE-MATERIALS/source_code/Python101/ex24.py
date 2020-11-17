def is_even(a):
  if a%2==0:
    return 1
  return 0

def sum_of_squares_odd_even(n):
  odd_sum=0
  even_sum=0
  
  for i in range(1,n+1):
    if is_even(i)==1:
      even_sum=even_sum+i**2
    else:
      odd_sum=odd_sum+i**2
  
  print('Sum of squares for odd numbers',odd_sum)
  print('Sum of squares for even numbers',even_sum)

num=int(input('Enter a number:'))
sum_of_squares_odd_even(num)