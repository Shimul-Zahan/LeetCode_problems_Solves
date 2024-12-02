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
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
            
class Solution(object):
    def isPalindrome(self, head):
        array_of_nodes = []
        while head:
            array_of_nodes.append(head.val)
            head = head.next.next
        print(array_of_nodes)
    
ll = LinkedList(1)
ll.append(2)
# ll.append(5)
# ll.append(7)
# ll.print()

s = Solution()
s.isPalindrome(ll.head)