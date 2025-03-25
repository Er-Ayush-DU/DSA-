class Node:
    def __init__(self,item):
        self.item=item
        self.next=None 

class SinglyList:
    def __init__(self):
        self.head=None


    def insert_head(self,new_item):
        new_node= Node(new_item)
        new_node.next=self.head
        self.head=new_node

    # def append(self,new_item):
    #     new_node= Node(new_item)
    #     if self.head==None:
    #         self.head=new_node
    #         return
    #     curr=self.head
    #     while curr.next!=None:
    #         curr=curr.next
    #     curr.next=new_node

    def append(self,new_item):
        new_node= Node(new_item)
        curr=self.head
        while curr.next!=None:
            curr=curr.next
            if self.head==None:
              self.head=new_node
        curr.next=new_node


    def insert_any_position(self,new_item,after):
        new_node= Node(new_item)
        curr=self.head
        while curr!=None:
            if curr.item ==after:
                break
            curr=curr.next       
        if self.head==None:
            return "Singly List is Empty"
        elif curr.next==None:
                return "item is not found"
        elif curr!= None:
            new_node.next=curr.next
            curr.next=new_node
    
    def delete_head(self):
        if self.head==None:
            return "linked list is empty"
        else:    
         self.head=self.head.next              

    def pop(self):
        if self.head==None:
            return "linked list is empty"
        else:
            curr=self.head
            while curr.next.next!=None:
                curr=curr.next
            curr.next=None        

    def delete_any_position(self,data):
           curr=self.head
           while curr.next!=None:
              if curr.item==data:
                break
              curr=curr.next 
           
           if curr.next==None:
              return "item is not found"
           elif self.head==None:
              return "linked list is empty"
           else:
              curr.next=curr.next.next
                


              


    def traverse(self):
        curr=self.head
        while curr:
            print(curr.item,end=" <-> ")
            curr=curr.next
        print(None)

sl=SinglyList()
sl.insert_head(10)
sl.insert_head(20)
sl.insert_head(30)

sl.append(50)
sl.append(60)

# sl.insert_any_position(100,10)

# sl.delete_head()

# sl.pop()

sl.delete_any_position(10)

sl.traverse()
        


    