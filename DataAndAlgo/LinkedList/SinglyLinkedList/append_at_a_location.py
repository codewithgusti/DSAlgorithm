class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self) :
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
    def append_at_a_location(self,data,index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
       
        while current:
            if count == 1:
               node.next = current
               self.head = node
               print(count)
               return
           
            elif index == index:
                node.next = current
                prev.next = node
                return
            
            count +=1
            prev=current
            current = current.next
            
        if count < index :
           print('The List has less number of elements')
    
    def append_at_location_data(self,data):
        current = self.head
        prev = self.head
        node = Node(data)
        
        while current:
            if current.data ==data:
                node.next = current
                prev.next = node
            
            prev = current
            current = current.next          
           
words = SinglyLinkedList()
words.append('eggs')
words.append('spam')
words.append('ham')
words.append('fish')
words.append_at_a_location('meat', 2)
words.append_at_location_data('ham')

current = words.head
while current:
    print(current.data)
    current = current.next
    
            
        