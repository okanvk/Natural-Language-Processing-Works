while True:
  password=input('Enter password')
  
  if len(password) in range(4,8):
    print('Your password is: ', password)
    break
  else:
    print('Password is invalid. Try again')