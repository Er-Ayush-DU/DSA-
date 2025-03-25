#  Using linked list

class Node:
  def __init__(self,item):
    self.item=item
    self.top=None


class Stack:
  def __init__(self):
    self.top=None


  def is_empty(self):
    return self.top==None

  def pop(self):
    if self.is_empty():
      return "stack is empty"
    else:
        data= self.top.item
        self.top=self.top.next
        return data

  def push(self,new_item):
    new_node= Node(new_item)
    new_node.next=self.top
    self.top=new_node

  def peak(self):
    if self.is_empty():
      return "stack is empty"  
    else:
      print("top element of Stack is",self.top.item)

 

  def display(self):
    curr=self.top
    while curr!=None:
      print(curr.item, end="  ")  
      curr=curr.next    

      

S= Stack()
S.push(10)
S.push(20)
S.push(30)
S.push(40)

S.pop()
S.peak()


S.display()





# Using List


class Stack:
    def __init__(self):
        self.data=[]
    def is_empty(self):
        return len(self.data)==0
        
    def Push(self,item):
        self.data.append(item)

    def Pop(self):
        if not self.is_empty():
          return self.data.pop()
        else:
            raise IndexError("stack is empty")

    def Peek(self):
        if not self.is_empty():
         return self.data[-1]
        else:
            raise IndexError("stack is empty")

    def Size(self):
        return len(self.data)

   
        
        
  

S= Stack()
S.Push(10)
S.Push(20)
S.Push(30)


print(S.Peek())
print(S.Pop())
print(S.Peek())

print(S.Size())
