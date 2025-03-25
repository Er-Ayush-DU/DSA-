class Node:
    def __init__(self,value):
        self.prev= None
        self.data= value
        self.next= None

class DoublyLinkedList:
    def __init__(self):
        self.head= None

    def Insert_at_head(self,new_value):
        new_node= Node(new_value)
        if self.head!=None:
            new_node.next=self.head
            self.head.prev= new_node
        self.head= new_node



    def Insert_at_tail(self,new_value):
        new_node= Node(new_value)
        curr= self.head
        while curr.next!= None:
            curr= curr.next

        if curr.next== None:
            new_node.prev= curr
            curr.next= new_node
        else: 
            #  when head is None
            return "doubly linked list is Empty" 

    
    def insert_after(self, after,new_value):
        new_node= Node(new_value)
        curr= self.head
        while curr.next!= None:
            if curr.data==after:
                new_node.next = curr.next
                new_node.prev = curr 
                if curr.next is not None:  # Adjust the next node's previous pointer if it exists
                    curr.next.prev = new_node
                curr.next = new_node       # Set current node's next to the new node
                return
            curr = curr.next
        print(f"Node with value {after} not found.") 

    def Display(self):
        curr= self.head
        while curr!=None:
            print(f"[{curr.prev.data if curr.prev else None} <-  {curr.data} -> {curr.next.data if curr.next else None}]" , end=" <=> ")
            curr= curr.next

        print("None")

    def delete_head(self):
        if self.head is None:
            print("Doubly Linked List is Empty")

        if self.head.next is None:
            self.head= None
            return

        self.head=self.head.next
        self.head.prev=None  


    def delete_tail(self):
        if self.head is None:
            print("Doubly Linked List is Empty")

        if self.head.next is None:
            self.head= None
            return 

        curr= self.head
        while curr.next!=None:
            curr=curr.next

        if curr.prev is not None:
         curr.prev.next= None
        curr.prev= None   


    def delete_any_postion(self,after):
        curr=self.head
        while curr.next!=None:
            if curr.data==after:
                break
            curr= curr.next
        curr.prev.next=curr.next
        curr.next.prev=curr.prev




Dl= DoublyLinkedList()
Dl.Insert_at_head(10)
Dl.Insert_at_head(20)
Dl.Insert_at_head(30)


# Dl.Insert_at_tail(60)
Dl.Insert_at_tail(70)

# Dl.insert_after(60,100)
Dl.insert_after(20,100)

# Dl.delete_head()

# Dl.delete_tail()

Dl.delete_any_postion(20)


Dl.Display()
            
           