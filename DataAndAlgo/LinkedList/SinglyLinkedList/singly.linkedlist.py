
class Node :
    def __init__(self,data = None):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
    
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

words = SinglyLinkedList()
words.append('apple')
words.append('banana')
words.append('orange')

current = words.head
while current:
    print(current.data)
    current= current.next