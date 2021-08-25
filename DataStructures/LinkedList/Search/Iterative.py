from DataStructures.LinkedList.LinkedListConstruct import Node, createdLinkedList

list = createdLinkedList()
data = list.iterativeSearch(Node(3))
if data > -1:
    print("Node is found at {}".format(data))
else:
    print("No such node is found!")
