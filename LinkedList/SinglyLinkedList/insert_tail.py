# INSERT FROM TAIL

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head= None

    def insert_tail(self,new_value):
        new_node= Node(new_value)

    #If Linked list is Empty
        if self.head==None:
         self.head=new_node
         return

     # If linked list is not empty
        last = self.head
        while last.next:
            last=last.next

        last.next=new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print(None)

     


  
   
L= LinkedList()      
L.insert_tail(10)
L.insert_tail(10)
L.insert_tail(50)
L.display()
        
        
