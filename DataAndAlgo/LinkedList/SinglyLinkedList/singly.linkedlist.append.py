
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
            
    def append_at_a_location(self,data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
        while current:
            if count == 1:
                node.next = current
                self.head = node
                return
            
            elif index == index:
                node.next = current 
                prev.next = node
                return
            count +=1
            prev=count
            count=count.next
        if count < index:
            print('The list has less number of elements')
        
        

words = SinglyLinkedList()
words.append('apple')
words.append('banana')
words.append('orange')
words.append_at_a_location('new',2)

current = words.head
while current:
    print(current.data)
    current= current.next