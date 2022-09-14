class Node:

  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

  def print(self):
    print(self.data,end='')    



def Stack_Print(top):
  current_node=top
  print('top->',end='')
  while current_node:
    current_node.print()
    print('->',end='');
    current_node=current_node.next
  print('(None)  ',end='')
  print('Length ',Stack_Length(top))



def Stack_Push(top,data):
  top=Node(data,top)
  print(data,'is pushed')
  return top



def Stack_Pop(top):
  node=top
  if node:
    top=top.next
    print(node.data,'is popped')
  else:
    print('Stack is Empty')
  return top,node
  


def Stack_Length(top):
  current_node=top
  n=0
  while current_node:
    n+=1
    current_node=current_node.next
  return n     



# inititlalize
top=None



# push data
top=Stack_Push(top,1)

Stack_Print(top)

top=Stack_Push(top,2)

Stack_Print(top)

top=Stack_Push(top,3)

Stack_Print(top)



# pop data
top,popped=Stack_Pop(top)

Stack_Print(top)

top,popped=Stack_Pop(top)

Stack_Print(top)

top,popped=Stack_Pop(top)

Stack_Print(top)



# Empty pop
top,popped=Stack_Pop(top)


