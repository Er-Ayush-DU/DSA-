def reverse(data):
  list = []
  
  for char in data:
    list.append(char)
    
  rev_list = " " 
  
  while list:
    rev_list += list.pop()
  print(rev_list)
    
    
data = "Ayush"    
    
reverse(data)
