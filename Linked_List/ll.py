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
            
            
ll = LinkedList(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.print()
        
        
        
        
        
        
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