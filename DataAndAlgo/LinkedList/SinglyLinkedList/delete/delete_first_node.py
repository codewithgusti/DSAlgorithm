
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
            
    def delete_first_node(self):
        current = self.head
        if self.head is None:
            print('There is no elements to delete')
        elif current == self.head:
            self.head = current.next
        
    

words = SinglyLinkedList()
words.append('eggs')
words.append('spam')
words.append('ham')
words.append('fish')
words.delete_first_node()

current = words.head
while current:
    print(current.data)
    current = current.next
