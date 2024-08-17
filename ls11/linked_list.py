class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return f'{self.data}'

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = None
    
    
    def __iter__(self): 
        self.current = None
        return self
    

    def __next__(self):
        if self.current is None:
            self.current = self.head
            return self.head
        self.current = self.current.next

        if self.current is None:
            raise StopIteration
        else:
            return self.current
    

    def __len__(self):
        i, current = 0, self.head
        while current:
            i += 1
            current = current.next
        return i


    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


    def remove(self, value):
        current = self.head
        while current.next:
            if current.next.data == value:
                if current.next.next is not None:
                    current.next = current.next.next
                else:
                    current.next = None
            current = current.next


    def pop(self, value=None):
        if value is None:
            value = len(self) - 1
        i = 0
        prev = None
        current = self.head
        
        while i != value:
            if current.next:
                prev = current
                current = current.next
                i += 1
            else: 
                break
        else: 
            if current.next:
                prev.next = current.next
            else:
                prev.next = None
        
                

ll = LinkedList()
ll.append(12)
ll.append(13)
ll.append(14)
ll.append(15) 
for el in ll:
    print(el)

print(len(ll))

print(13 in ll)
print(12 in ll)

ll.remove(14)

for el in ll:
    print(el)

ll.pop()

print("-----")
for el in ll:
    print(el)