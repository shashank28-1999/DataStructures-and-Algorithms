#Level order raversal in a binary tree
from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def levelorder(root):
    q=deque()
    l=[]
    if(root==None):
        return l
    q.append(root)
    while(q):
        levelnum=len(q)
        l1=[]
        for i in range(0,levelnum):
            x=q.popleft()
            if(x.left is not None):
                q.append(x.left)
            if(x.right is not None):
                q.append(x.right)
            l1.append(x.value)
        l.append(l1)
    return l

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("level order elements")
print(levelorder(root))
