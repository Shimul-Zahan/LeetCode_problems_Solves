# Kth BST Value

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST

# create node for a tree
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
        
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#         self.length = 0

#     def insert(self, value):
#         new_node = Node(value)
#         if self.root is None:
#             self.root = new_node
#             self.length += 1
#             return True
#         temp = self.root
#         while(True):
#             if new_node.value == temp.value:
#                 return False
#             if new_node.value < temp.value:
#                 if temp.left is None:
#                     temp.left = new_node
#                     self.length += 1
#                     return True
#                 temp = temp.left
#             if new_node.value > temp.value:
#                 if temp.right is None:
#                     temp.right = new_node
#                     self.length += 1
#                     return True
#                 temp = temp.right

class Solution(object):
    def kthSmallest(self, root, k):
        
        def in_order_helper(root, array):
            if root:
                in_order_helper(root.left, array)
                array.append(root.val)
                in_order_helper(root.right, array)

        array = []
        in_order_helper(root, array) 
        if 0 < k <= len(array):
            return array[k - 1] 
        return None
        