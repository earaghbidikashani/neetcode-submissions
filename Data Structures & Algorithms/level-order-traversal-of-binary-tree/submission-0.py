# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        res = []

        while q:
            temp = len(q)
            resss = []
            for _ in range(temp):
                curr = q.popleft()
                if curr is None:
                    continue
                resss.append(curr.val)

                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            
            res.append(resss)

        return res