# linked list


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = LinkedListNode(data)
        currentNode = self.head
        if(currentNode is None):
            currentNode = newNode
            return
        while(currentNode is not None):
            current = current.next
        current = newNode
