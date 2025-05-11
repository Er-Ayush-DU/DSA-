class Node:
    def __init__(self,value):
        self.data=value
        self.next= None

class Queue:
    def __init__(self):
        self.front=None
        self.rear= None

    def Enqueue(self, new_value):
        new_node = Node(new_value)
        if self.rear==None:
            self.front=  new_node
            self.rear=self.front

        else:
            self.rear.next= new_node
            self.rear=new_node


    def Dequeue(self):
        if self.front==None:
            return "Queue is Empty"

        else:
            self.front= self.front.next


              #Display

    def Display(self):
        curr= self.front
        while curr !=None:
            print(curr.data)
            curr= curr.next
     


Q= Queue()
Q. Enqueue(10)
Q. Enqueue(20)
Q. Enqueue(30)
Q. Enqueue(40)

Q.Dequeue()

Q.Display()



