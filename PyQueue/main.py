class Node:

  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

  def print(self):
    print(self.data,end='')    



def Queue_Print(top):
  current_node=top
  print('back->',end='')
  while(current_node):
    current_node.print()
    print('->',end='');
    current_node=current_node.next
  print('front')



def enqueue(head,data):
  head=Node(data,head)
  print(data,'is enqueued')
  return head



def dequeue(head):
  current_node=head
  node=Node
  if current_node:
    if current_node.next:
      while current_node.next:
        node=current_node
        current_node=current_node.next
      data=current_node.data
      node.next=current_node.next
      node=current_node
    else:
      node=current_node
      data=node.data
      head=current_node.next
    print(data,'is dequeued')  
  else:
    print('Empty Queue')    
  return head,node
    




# inititlalize
head=None



# enqueue data

head=enqueue(head,1)

Queue_Print(head)

head=enqueue(head,2)

Queue_Print(head)

head=enqueue(head,3)

Queue_Print(head)



# enqueue data

head,dequeued=dequeue(head)

Queue_Print(head)

head,dequeued=dequeue(head)

Queue_Print(head)

head,dequeued=dequeue(head)

Queue_Print(head)



# Empty dequeue

head,dequeued=dequeue(head)
