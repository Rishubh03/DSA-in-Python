#linked List Delete node at the end

def deletell(self):
    temp = self.head 
    if(temp.next == None):
      del temp.data
      return
    while temp.next is not None:
      prev = temp
      temp = temp.next

    del temp.data
    prev.next = None 

#Stack Implementation using Linkedlist

class Node:
  def __init__(self,val):
    self.data = val
    self.next = None

class Linkedlist:
  def __init__(self):
    self.head = None

  def printll(self):
    temp = self.head
    while temp is not None:
      print(temp.data)
      temp = temp.next
  
  def push(self,val):
    temp = self.head

    while temp.next is not None:
      temp = temp.next
    new_node = Node(val)
    temp.next = new_node






  def pop(self):
    temp = self.head 
    if(temp.next == None):
      del temp.data
      return
    while temp.next is not None:
      prev = temp
      temp = temp.next

    del temp.data
    prev.next = None 



ll = Linkedlist()
ll.head = Node(10)

while(True):
  opt = int(input(" 1. push \n 2. Pop \n 3. Print \n "))
  if opt == 1:
    ll.push(int(input("Enter the element ")))
  elif opt ==2:
    ll.pop()
  elif opt == 3:
    ll.printll()
     

