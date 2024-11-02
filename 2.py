# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
            
    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
            
class Solution(object):
    def isPalindrome(self, l1, l2):
        array_of_nodes1 = []
        array_of_nodes2 = []
        int1 = 0
        int2 = 0
        while l1:
            array_of_nodes1.append(l1.val)
            l1 = l1.next
                    
        while l2:
            array_of_nodes2.append(l2.val)
            l2 = l2.next
            
        result = ''.join(str(int(''.join(map(str, array_of_nodes1[::-1]))) + int(''.join(map(str, array_of_nodes2[::-1])))))
        arr = []
        for i in range(len(result)):
            arr.append(result[i])
        print(arr[::-1])
            
        
        
    
ll = LinkedList(1)
ll.append(2)
ll.append(5)
ll.append(4)
# ll.append(5)
# ll.append(7)
# ll.print()

s = Solution()
s.isPalindrome(ll.head, ll.head)