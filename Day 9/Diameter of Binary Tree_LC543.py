def diameterOfBinaryTree(self, root):
    if not root:
        return 0
    res = [0]
    def getHeight(node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        l = getHeight(node.left)
        r = getHeight(node.right)
        res[0] = max(res[0],l+r)
        return 1 + max(l , r)
    getHeight(root)
    return res[0]