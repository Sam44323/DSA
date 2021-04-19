from LinkedList import Node, LinkedList

if __name__=='__main__':
  
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
  
    llist.head.next = second
    second.next = third
    third.next= fourth

    llist.printList()
    print('*'*30)
    print(' ')

  # deleting a node from the list

    llist.deleteItem(2)
    llist.printList()
    print('*'*30)
    print(' ')