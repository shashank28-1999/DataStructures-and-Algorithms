#Return maximum sum form a path in a tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

def maxpath(root):
    if(root is None):
        return
    if root.left is None and root.right is None:
        return root.value
    
    leftsum=maxpath(root.left)
    rightsum=maxpath(root.right)
    
    return root.value+max(leftsum,rightsum)

print("maximum sum in the tree is ",maxpath(root))
