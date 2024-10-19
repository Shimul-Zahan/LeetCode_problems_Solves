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
    def isPalindrome(self, head, left, right):
        temp = head
        before = None
        
        while temp:
            next_node = temp.next
            temp.next = before
            before = temp
            temp = next_node
        return before
    
ll = LinkedList(1)
ll.append(2)
ll.append(5)
ll.append(7)
# ll.print()

s = Solution()
reversed_head = s.isPalindrome(ll.head, 1, 3)
temp = reversed_head
while temp:
    print(temp.val)
    temp = temp.next
    
    
    
# original  Solution
# temp = head
#         before = None
        
#         while temp:
#             next_node = temp.next
#             temp.next = before
#             before = temp
#             temp = next_node
#         return before