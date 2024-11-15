# DELETE FROM HEAD

class Node:
    def __init__(self,value):
        self.data= value
        self.next=None

class LinkedList:
    def __init__(self):
     self.head= None

    def Insert_head(self,new_value):
        new_node= Node(new_value)
        new_node.next= self.head
        self.head= new_node

    def del_head(self):
        if self.head== None:
            return "Linked List is Empty"

        self.head= self.head.next


    def display(self):
        curr= self.head
        while curr:
            print(curr.data, end= "->")
            curr= curr.next
        print('None')
         

       
                  

    

L=LinkedList()
L.Insert_head(10)
L.Insert_head(20)
L.Insert_head(30)
L.display()
L.del_head()
L.display()
        
