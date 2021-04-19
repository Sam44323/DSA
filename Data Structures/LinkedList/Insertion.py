from LinkedList import Node, LinkedList

if __name__=='__main__':
  
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
  
    llist.head.next = second; 
    second.next = third; 

    # inserting from front
    llist.push(4)
    llist.printList()
    print('*'*30)

    # inserting in between
    llist.insertBtw(second, 8)
    llist.printList()