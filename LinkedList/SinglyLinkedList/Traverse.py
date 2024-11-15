                              # TRAVERSING

#create a node 
class node:
    def __init__(self,value):
        self.data= value
        self.next= None

#Create a Empty Linked List
class LinkedList:
    def __init__(self):
        self.head= None
        self.n= 0
        
    def __len__(self):
       return self.n
        
#  Insertion 
    def Insert_head(self,new_value):
    #create a new node 
     new_node= node(new_value)

    #create a connection
     new_node.next= self.head

    # reassign head
     self.head=new_node

    #Increment
     self.n= self.n+1

# Traversing

    def traverse(self):
      curr= self.head
      # while curr!=None:
      #   print(curr.data , end= "-> ")
      #   curr= curr.next

      while curr:
        print(curr.data , end= "-> ")
        curr= curr.next
      print(None)
            
        


L= LinkedList()
L.Insert_head(1)
L.Insert_head(2)
L.Insert_head(3)
L.Insert_head(4)
L.Insert_head(5)

# len(L)

L.traverse()
    
    
    