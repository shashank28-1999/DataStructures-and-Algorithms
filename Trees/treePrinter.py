#This is used to print trees in level order
from collections import deque
def printTree(root):
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        for _ in range(level_size):
            node = q.popleft()
            print(node.value, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()