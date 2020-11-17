operation=input('Select operation (+, -, *, /)')

num1=int(input('Enter first number'))
num2=int(input('Enter second number'))

if operation=='+':
  result=num1+num2
elif operation=='-':
  result=num1-num2
elif operation=='*':
  result=num1*num2
elif operation=='/':
  result=num1/num2
else:
  print('You entered an undefined operation')

print('Result:', result)