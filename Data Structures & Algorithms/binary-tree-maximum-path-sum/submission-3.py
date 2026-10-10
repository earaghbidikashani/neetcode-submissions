class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = float("-inf")
        def dfs(node):
            nonlocal maxx

            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            maxx = max(maxx, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return maxx

            