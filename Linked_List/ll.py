class Node:
    def __init__(self, value):
        self.value = value   #!value here
        self.next = None     #!pointer here
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, target):
        if target < 0 or target >= self.length:
            return None
        temp = self.head
        for _ in range(target):
            temp = temp.next
        return temp
    
    def set_value(self, target, value):
        temp = self.get(target)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, target, value):
        if target < 0 or target >= self.length:
            return None
        if target == 0:
            return self.prepend(value)
        if target == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(target - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, target):
        if target < 0 or target >= self.length:
            return None
        if target == 0:
            return self.pop_first()
        if target == self.length:
            return self.pop()
        prev = self.get(target - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -+ 1
        return True
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        
        
            
            
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.prepend(5)
# ll.pop_first()
ll.print()
# ll.insert(2, 500)
ll.remove(2)
# print(ll.get(2), "get the targeted element")
# print(ll.set_value(2, 100), "get the targeted element")
ll.print()
# print(ll.pop(), "popped item")
# print(ll.pop(), "popped item")
# print(ll.pop(), "popped item")
# print(ll.pop(), "popped item")
        
        
        
        
        
        
# * Here is common concepts ****************
    # Always remeber the dictionary
    # The key is the node's value 
    # The value is the node itself
    # The 'next' pointer is used to link nodes together
    # '''
    #     {
    #         "value": 4,
    #         "next": {
    #             "value": 2,
    #             "next": {
    #                 "value":10,
    #                 "next": None
    #             },
    #         },
    #     }
    # '''