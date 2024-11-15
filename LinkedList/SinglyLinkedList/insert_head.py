  # INSERT FROM HEAD

class Node:
    def __init__(self, value):
        self.data=value
        self.next=None

# create a empty linked list
class LinkedList:
    def __init__(self):
        self.head=None

# Insert from Head

    def Insert_from_head(self,new_value):
        new_node= Node(new_value)

        new_node.next= self.head
        self.head= new_node

# display the Nodes

    def print_LL(self):
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print(None)

L= LinkedList()
L.Insert_from_head(10)
L.Insert_from_head(20)
L.Insert_from_head(30)
L.print_LL()