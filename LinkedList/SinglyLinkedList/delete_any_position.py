# DELETE AT ANY POSITION

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

    def del_tail(self):
         curr=self.head
         while curr.next.next!= None:
          curr= curr.next
         curr.next=None



    def At_any_position(self,item):
        curr= self.head
        while curr.next!= None:
            if curr.next.data== item:
                break
            curr= curr.next

        if curr.next== None:
            return 'item is not Found'
        else:
            curr.next=curr.next.next
    
                
    
       

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
L.Insert_head(40)
L.Insert_head(50)

L.display()

L.At_any_position(30)
L.At_any_position(40)


L.display()


        
