
class Node :
    def __init__(self, data = None) :
        self.data = data
        self.next = None

class SinglyLinkedList :
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
    
    def append(self , data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail =node
            self.head = node
    def length(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count

words = SinglyLinkedList()
words.append('eggs')
words.append('spam')
words.append('ham')
words.append('fish')
print(words.length())

current = words.head
while current:
    print(current.data)
    current = current.next
