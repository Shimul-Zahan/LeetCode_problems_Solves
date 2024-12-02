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
        fast = head
        last = head
        while fast and fast.next:
            last = last.next
            fast = fast.next.next
            
        prev = None
        while last:
            next_node = last.next
            last.next = prev
            prev = last
            last = next_node
            
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
    
ll = LinkedList(1)
ll.append(2)
ll.append(5)
ll.append(7)
# ll.print()

s = Solution()
s.isPalindrome(ll.head)


# Best solution
# Solutions Here
# def isPalindrome(self, head):
#         arrayofflist = []
        
#         while head:
#             arrayofflist.append(head.val)
#             head = head.next
        
#         print(arrayofflist, "original array")
#         print(arrayofflist[:: -1], "reverse array")
        
#         if arrayofflist == arrayofflist[:: -1]:
#             print(True, "from sol")
#         else:
#             print(False, "from sol")

        