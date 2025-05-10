import heapq

class Min_heap: 
  def __init__(self):
    self.heap = []
    
  def insert(self , val):
    heapq.heappush(self.heap , val) 
    return self.heap
    # print(self.heap)  
    
  def delete(self):
    if len(self.heap)==0: 
      return None
    removed = heapq.heappop(self.heap)
    return removed
  
    
  def Min(self):
    return self.heap[0] if self.heap else None  
  
  
  def display(self):
    print (self.heap)
    
    
    
H = Min_heap()

# for min_heap in [50,60,10,5,40,30]:
#  H.insert(min_heap)

H.insert(50)
H.insert(60)
H.insert(10)
H.insert(5)
H.insert(40)
H.insert(30)

print("Min Heap val is: " , H.Min()) 

print("delete value is" , H.delete())

H.display()