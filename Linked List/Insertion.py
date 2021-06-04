#Linked List Implementation

class Node:
  def __init__(self, val):
    self.data = val
    self.next = None


class Linkedlist:
  def __init__(self):
    self.head = None

  def llprint(self): #linked List print
    temp = self.head

    while temp is not None:
      print(temp.data)
      temp=temp.next

  def begpush(self, val): #push at  beginning 
    nnode = Node(val)

    nnode.next=self.head

    self.head = nnode

  def endpush(self,val): #push at the end
    nnode = Node(val)
    temp = self.head

    while temp.next is not None:
      temp = temp.next 
    temp.next = nnode

        
ll = Linkedlist()
ll.head = Node(10)
second = Node(15)
third = Node(20)

ll.head.next = second
second.next = third
ll.endpush(40)
ll.begpush(61)

ll.llprint()
