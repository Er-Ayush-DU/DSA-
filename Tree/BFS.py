from collections import deque

class Node:
  def __init__(self, data):
   self.left =None
   self.right = None
   self.data = data
   
  @staticmethod
  def BFS(root):
    if root is None:
      return
    
    queue = deque([root])
    
    while queue:
      node = queue.popleft()
      print(node.data , end = " ")
      
      if node.left:
        queue.append(node.left)
        
      if node.right:
        queue.append(node.right)  
        
        
if __name__  == "__main__" :
    
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    
    root.left.left = Node(80)
    root.left.right = Node(60)
    
    root.right.left = Node(70)
    root.right.right = Node(40)
    
    Node.BFS(root)        
        
        
 
    
    
   