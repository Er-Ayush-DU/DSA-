# INSERT AT ANY POSTION

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head= None


    def insert_tail(self,new_value1):
        new_node= Node(new_value1)

    #If Linked list is Empty
        if self.head==None:
         self.head=new_node
         return

     # If linked list is not empty
        last = self.head
        while last.next:
            last=last.next

        last.next=new_node
        return


        

    def insert_any_postion(self,after,new_value2):
        new_node= Node(new_value2)

        curr= self.head
        while curr!= None:
            if curr.data== after:
                break
            curr= curr.next

        if curr is not None:
            new_node.next= curr.next
            curr.next= new_node
        else:
            print("Item is not Found")
            
        
    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print(None)    




  
   
L= LinkedList()
L.insert_tail(2)
L.insert_tail(10)
L.insert_tail(7)
L.insert_tail(20)



L.insert_any_postion(7,200)
L.insert_any_postion(8,200)
L.insert_any_postion(10,50)
L.insert_any_postion(5,200)

L.display()
        


        