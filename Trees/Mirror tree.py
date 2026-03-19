#Generate mirror image of the tree
from treePrinter import printTree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def mirror(root):
    if(root==None):
        return 
    mirror(root.left)
    root.left,root.right=root.right,root.left
    mirror(root.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("before mirroring : ")
printTree(root)
mirror(root)
print("after mirroring : ")
printTree(root)