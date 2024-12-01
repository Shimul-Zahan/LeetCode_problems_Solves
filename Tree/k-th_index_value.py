class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0
        
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.length += 1
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    self.length += 1
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    self.length += 1
                    return True
                temp = temp.right
        
    def in_order_traversal(self, root, index):
        array = []
        self.in_order_helper(root, array) 
        if 0 < index <= len(array):
            return array[index - 1] 
        return None

    def in_order_helper(self, root, array):
        if root:
            self.in_order_helper(root.left, array)
            array.append(root.value)
            self.in_order_helper(root.right, array)

            
bst = BinarySearchTree()
root = [3,1,4,None,2]
for value in root:
    if value is not None:
        bst.insert(value)
        
# print("The root of the tree is:")
# print(bst.root.value)
print("In-order Traversal:")
index = 1
array = bst.in_order_traversal(bst.root, index) 
print(array)
# Get in-order traversal in an array
# inorder_array = bst.in_order_traversal(bst.root)
# print("In-order Traversal:", inorder_array)