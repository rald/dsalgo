class Node:

  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

  def print(self):
    print(self.data,end='')    



def LinkedList_Print(head):
  current_node=head
  print('head->',end='')
  while current_node:
    current_node.print()
    print('->',end='');
    current_node=current_node.next
  print('(None)  ',end='')
  print('Length',LinkedList_Length(head))



def LinkedList_Length(head):
  current_node=head
  n=0
  while current_node:
    n+=1
    current_node=current_node.next
  return n




# initialize
one=Node(1)
two=Node(2)
three=Node(3)



# connect
one.next=two
two.next=three
three.next=None



# print
head=one
LinkedList_Print(head)



