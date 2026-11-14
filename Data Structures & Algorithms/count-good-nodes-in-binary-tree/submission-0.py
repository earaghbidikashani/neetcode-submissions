# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def dfs(node, biggest):
            nonlocal total
            
            if node is None:
                return
            
            if node.val >= biggest:
                total += 1
                biggest = node.val

            dfs(node.left, biggest)
            dfs(node.right, biggest)

        dfs(root, root.val)

        return total