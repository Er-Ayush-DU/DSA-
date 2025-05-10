class Min_Heap:
  def __init__(self):
    self.heap = []
    
    
  def insert(self, val):
    self.heap.append(val)
    self.heapifyUp(len(self.heap)-1)
    
  def delete(self):
    if len(self.heap)==0:
      return None
    if len(self.heap)==1:
      return self.heap.pop()  
    
    root = self.heap[0] 
    self.root[0] = self.heap.pop()
    self.heapifyDown(0)
    return root
  
  
  def heapifyUp(self,index):

      parent = (index-1)//2
      
      if index>0 and self.heap[index]< self.heap[parent]:
        self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
        self.heapifyUp(parent)
        
  def heapifyDown(self , index):
   smallest = index
   left = 2*index +1
   right = 2*index+2
   
   if  left < len(self.heap) and self.heap[left] < self.heap[smallest]:
     smallest = left   
     
   if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
     smallest = right
     
   if smallest != index:
     self.heap[smallest] , self.heap[index] =  self.heap[index] ,  self.heap[smallest] 
     self.heapifyDown(smallest)
     
     
  def display(self):
    print (self.heap )  
    
    
M = Min_Heap()

M.insert(20)
M.insert(60)
M.insert(50)
M.insert(40)
M.insert(65)

M.display()

