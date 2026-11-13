# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        if p.val > q.val:
            bigg = p
            small = q
        else: 
            bigg = q
            small = p

        while bigg.val < curr.val or small.val > curr.val:
            if bigg.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return curr