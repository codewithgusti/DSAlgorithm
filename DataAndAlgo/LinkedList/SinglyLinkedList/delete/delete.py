

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
            
    def delete(self,data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if  current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                    self.size -=1
                return
            
            prev = current
            current = current.next
    
words = SinglyLinkedList()
words.append('eggs')
words.append('spam')
words.append('ham')
words.append('fish')
words.delete('ham')

current = words.head
while current:
    print(current.data)
    current = current.next
