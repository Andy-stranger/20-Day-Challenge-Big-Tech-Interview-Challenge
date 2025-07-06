def maxPathSum(self, root):
    if not root:
        return 0
    maxi = [root.val]
    def get_max_sum(node):
        if not node.left and not node.right:
            return node.val
        left_max , right_max = float("-inf") , float("-inf")
        if node.left:
            left_max = get_max_sum(node.left)
        if node.right:
            right_max = get_max_sum(node.right)
        maxi[0] = max(maxi[0] , left_max, right_max, node.val + max(left_max,0) + max(right_max,0))
        return node.val + max(left_max,right_max,0)
    get_max_sum(root)
    return maxi[0]