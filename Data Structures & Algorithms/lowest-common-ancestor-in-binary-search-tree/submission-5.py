# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(i, j, node):
            if i.val <= node.val <= j.val:
                return node

            if node.val >= j.val:
                return dfs(i, j, node.left)

            if node.val <= i.val:
                return dfs(i, j, node.right)

        if p.val >= q.val:
            return dfs(q, p, root)

        return dfs(p, q, root)