class  MaxHeap:
  def __init__(self):
    self.heap= []    
    
  def insert(self , val):
    self.heap.append(val)
    self.heapifyUp(len(self.heap)-1)    
    
  def delete(self):
    if len( self.heap)==0:
      return None  
    if len(self.heap) ==1:
      return self.heap.pop() 
    
    root = self.heap[0]
    self.heap[0]=self.heap.pop()
    self.heapifyDown(0)
    return root
  
  def heapifyDown(self, index):
    largest = index
    left =  2*index +1
    right = 2*index+2
     
    if left < len(self.heap) and self.heap[left]> self.heap[largest]:
      largest = left
      
    if right < len(self.heap)  and self.heap[right] > self.heap[largest]:
      largest = right             
      
      
    if largest!= index:
      self.heap[index] , self.heap[largest] = self.heap[largest] , self.heap[index]  
      self.heapifyDown(largest)
    
    
  def heapifyUp(self, index):
    parent = (index-1) //2
    
    if index>0 and self.heap[index] > self.heap[parent]:
      self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index] 
      self.heapifyUp(parent)
      
      
  def display(self): 
    print(self.heap) 
  
      
      
H = MaxHeap()

# for num in [10, 20, 50, 30, 40, 60, 70]:
#   H.insert(num)

  
H.insert(10)
H.insert(20)
H.insert(50)  
H.insert(30)
H.insert(40)
H.insert(60)
H.insert(70)

H.delete()
H.display()

     
      