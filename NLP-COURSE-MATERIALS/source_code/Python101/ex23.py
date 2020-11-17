def func(*params):  
  mult=1
  for i in params:    
    mult=mult*i
  return mult

mult=func(2,3,4,5,7)
print(mult)