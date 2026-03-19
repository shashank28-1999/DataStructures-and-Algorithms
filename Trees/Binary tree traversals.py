#Traversals in a binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def inorder(x):
    if x is not None:
        inorder(x.left)
        print(f"{x.value} ",end =" ")
        inorder(x.right)    
def preorder(x):
    if x is not None:
        print(f"{x.value} ",end =" ")
        preorder(x.left)
        preorder(x.right)    
def postorder(x):
    if x is not None:
        postorder(x.left)
        postorder(x.right)
        print(f"{x.value} ",end =" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

inorder(root)
print()
preorder(root)
print()
postorder(root)