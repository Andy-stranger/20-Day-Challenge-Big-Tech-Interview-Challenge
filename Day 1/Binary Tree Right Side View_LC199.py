from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    q = deque()
    res = []
    if root is None:
        return res
    q.append(root)
    while q:
        size = len(q)
        for i in range(size):
            cur = q.popleft()
            if i == size-1:
                res.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return res