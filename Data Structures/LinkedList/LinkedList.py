class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  # method for inserting at front

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  # method for inserting in between the nodes

  def insertBtw(self, prev_node, data):
    if prev_node is None:
      print("The given node doesn't exist")
      return
    
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  # method for adding a new node at the end
  def insertEnd(self, data):
    new_node = Node(data);
    if self.head is None:
      self.head = new_node
    
    # traversing to the end of the linked list

    last = self.head
    while (last.next):
      last = last.next
    
    last.next = new_node


  # method for printing the list

  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next
