from DataStructures.LinkedList.LinkedListConstruct import createdLinkedList

list = createdLinkedList()
data = list.searchNthNode(3)

if data > -1:
    print("The value is found at: {}".format(data))
else:
    print("Sorry! No such node is present!")
