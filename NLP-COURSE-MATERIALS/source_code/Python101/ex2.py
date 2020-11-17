a=int(input('First number:'))
b=int(input('Second number:'))
c=int(input('Third number:'))

if a>b:
  max=a
else:
  max=b
  
if max<c:
  max=c
  
print('Maximum number: ', max)