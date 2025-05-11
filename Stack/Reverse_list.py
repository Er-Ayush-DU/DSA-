def reverseList(arr):
  stack = []
  
  for i in range(len(arr)):
    stack.append(arr[i])
    
    
  rev_arr = []  
  
  while stack:
    rev_arr.append(stack.pop())
  print(rev_arr)
    
    

arr1 = [1,2,3,4]
reverseList(arr1)    
