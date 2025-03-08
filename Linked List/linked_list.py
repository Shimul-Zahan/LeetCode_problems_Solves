# Process -:
    # 1. First we need a create a class for construct the linked list
    # 2. 
    
''' 
here is the representation 
{
    value: 10,
    next: {
        value: 20,
        next: {
            value: 100,
            next: None,
        }
    }
}
'''


class Node:
    def __init__(self, value):
        self.value = value    # here we create this node with value and a pointer
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node   # define a head for entry point
        self.tail = new_node   # define a head for last node
        self.length = 1
        
        
    def print_list(self):
        temp = self.head  # here we get the entry point though we travers not
        # print(temp)
        while temp:  # We travers here
            print(temp.value)
            temp = temp.next
        print("---------------")
            
    def append(self, value):
        new_node = Node(value)
        # print("from append", self.head)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # add the node to the next pointer
            self.tail = new_node       # move the tail in the last node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        
        while temp.next:
            pre = temp   # sheser ager node dhorar jonne eta use korechi
            temp = temp.next
        self.tail = pre   # tail e pre k add kore diyechi
        self.tail.next = None  # tail er pointer ke faka kore diyechi
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if not self.head:
            return None
        
        temp = self.head
        next_node = temp.next
        
        if self.head is None:  # If the list is now empty, also update tail
            self.tail = None
        
        self.head = next_node
        self.length -= 1
        return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return None
        
        new_node = Node(value)
        index = self.get(index)
        index.value = value
        return True
    
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        
        indexed_node = self.get(index - 1)
        next_node = indexed_node.next
        
        indexed_node.next = new_node
        new_node.next = next_node
        return True
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        
        self.head = prev  # Update head to the new first node
        
        
        
        
        
        
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
# ll.print_list()
# ---------------- Pop Here ---------------
# ll.pop()
# ll.print_list()
# print(ll)
# --------------- Prepend Here -------------
# ll.prepend(100)
# ll.print_list()
# --------------- Pop first -------------
# ll.pop_first()
# ll.print_list()
# --------------- get -------------
# ll.get(2)
# ll.print_list()
# --------------- set -------------
# ll.set(2, 69)
# ll.print_list()
# --------------- set -------------
ll.insert(3, 69)
ll.print_list()

# --------------- reverse -------------
ll.reverse()
ll.print_list()