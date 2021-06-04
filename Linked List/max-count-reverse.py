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

  def reverse(self,link): #reverse 

    if link == None:
      return
    ll.reverse(link.next)
    print(link.data)

  def search(self,key): #search
    temp = self.head

    while temp is not None:
      if temp.data == key :
        return 1
      temp = temp.next 
    return 0
  
  def counter(self):
    temp = self.head
    count = 0

    while temp is not None:
      count +=1
      temp = temp.next

    return count

  def maxi(self):
    temp = self.head
    max = 0

    while temp is not None:
      if temp.data > max:
        max = temp.data
      temp = temp.next
    return max 
      


        
ll = Linkedlist()
ll.head = Node(10)
second = Node(15)
third = Node(20)

ll.head.next = second
second.next = third
ll.endpush(40)
ll.begpush(61)


ll.llprint()
print('\n\n')
ll.reverse(ll.head)

if ll.search(100) == 0:
  print("not found")
else:
  print("found")

print("\n\n\n")

print("Lenght ",ll.counter())
print("\n\n Maximum",ll.maxi())
