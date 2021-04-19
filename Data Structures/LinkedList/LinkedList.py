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
  
  # method for deleting a node from the linked list
  def deleteItem(self, key):

    temp = self.head # storing the head node of the linked list

    # when the head holds the key itself
    if temp is not None:
      if temp.data == key:
        # removing the node from the head

        self.head = temp.next
        temp = None
        return
    
    # Storing the data of the prev node and the current node that will be deleted
    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next

    # if the key is not present in the linked list
    if(temp == None):
      return

    # Unlinking the node from the linked list

    prev.next = temp.next
    temp = None

  # method for deleting a node based on the key provided for the node

  def deletePosNode(self, pos):

    # if the linked list is empty
    if(self.head == None):
      return

    # storing the head node of the linked list
    temp = self.head

    # for the removal of the head position node
    if pos == 0:
      self.head = temp.next
      temp = None
      return

    # storing the prev node of the to-be deleted node
    for i in range(pos - 1):
      temp = temp.next
      if temp is None:
        break
      
    # when the postion is more than the number of nodes
    if temp is None:
      return
    if temp.next is None:
      return

    next = temp.next.next

    # Unlinking the node by connecting the prev and the next node
    temp.next = next

  # method for printing the list

  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next
