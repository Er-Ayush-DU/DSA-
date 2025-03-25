class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        if data< self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
 

    # Inorder traversal

    def InorderTraversal(self):
        elements = []

        #visit left subtree
        if self.left:
            left_element = self.left.InorderTraversal()
            elements += left_element
        #visit middle element
        elements.append(self.data)
        #visit right subtree
        if self.right:
            right_element = self.right.InorderTraversal()
            elements += right_element

        return elements

    def PreorderTraversal(self):
         elements = []

         # visit middle elements
         elements.append(self.data)
        
         # visit left subtree
         if self.left:
             elements += self.left.PreorderTraversal()
            
         # visit right subtree
         if self.right:
             elements += self.right.PreorderTraversal()
        
         return elements

    def PostorderTraversal(self):
         elements = []
        
         # visit left subtree
         if self.left:
             elements += self.left.PostorderTraversal()
             
         # visit right subtree
         if self.right:
             elements += self.right.PostorderTraversal()

          # visit middle elements
         elements.append(self.data)
             
         return elements
        

def build_tree(elements):
        print("Building tree with: " , elements)
        root = BinarySearchTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i])
        return root   


if __name__ == '__main__':
    numbers= [17,4,1,20,9,23,18,34]
    root = build_tree(numbers)

    print("Inorder Traverse : ",root.InorderTraversal())
    print("Preorder Traverse : ",root.PreorderTraversal())
    print("Postorder Traverse : ",root.PostorderTraversal())
   
    pass
         
            
            
            
    
