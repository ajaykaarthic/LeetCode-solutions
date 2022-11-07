class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Traversing through the list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end='\t')
            temp = temp.next
    
    #Insert a node at the begining of the linked list
    def insertAtBeg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Set next pointer of previous node to the new node and new node to the mid
    def insert_at_mid(self, mid, data):
        if mid is None:
            return
        new_node = Node(data)
        new_node.next = mid.next
        mid.next = new_node
    

    def insertAtEnd(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.head = new_node
            return
        while temp.next:
            temp = temp.next
        temp.next = new_node


if __name__ == '__main__':

    llist = LinkedList()

    # Initializing the head node with data
    llist.head = Node(1)

    # Initializing consequtive nodes
    second = Node(2)
    third = Node(3)

    # Mapping nodes with address
    llist.head.next = second
    second.next = third
    llist.insertAtEnd(3)
    llist.insert_at_mid(third,99)
    llist.printList()
