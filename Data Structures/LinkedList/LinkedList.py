class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insertBtw(self, prev_node, data):
    if prev_node is None:
      print("The given node doesn't exist")
      return
    
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node


  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
  
    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
  
    llist.printList()