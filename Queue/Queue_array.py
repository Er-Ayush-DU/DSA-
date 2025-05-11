queue = []

def Enqueue(val):
  queue.append(val)
  
def Dequeue():
  queue.pop(0)
  
def Size():
  return len(queue)

def display():
 for i in range(len(queue)):
    print(queue[i])
    

Enqueue(10)    
Enqueue(20)   
Enqueue(30)   
Enqueue(40)   

Dequeue()

display()