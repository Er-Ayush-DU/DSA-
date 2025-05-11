class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
    
  @staticmethod
  def DFS(root):
    if root is None:
      return
    print(root.data , end = " ")
    Node.DFS(root.left)
    Node.DFS(root.right)
    
    
if __name__  == "__main__" :
    
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    
    root.left.left = Node(80)
    root.left.right = Node(60)
    root.right.left = Node(70)
    root.right.right = Node(40)
    
    Node.DFS(root)
    
    