def create_str_list():
  string_list=[]
  string=input('Enter a string')
  while string!='Q':
    string_list=string_list+[string]
    string=input('Enter a string')
  return string_list
  
lst=create_str_list()
print(lst)