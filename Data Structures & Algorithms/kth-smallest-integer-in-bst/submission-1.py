class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k

            if node is None:
                return None

            # 1. Search left subtree
            left = dfs(node.left)
            if left is not None:
                return left

            # 2. Process current node
            k -= 1
            if k == 0:
                return node.val

            # 3. Search right subtree
            return dfs(node.right)

        return dfs(root)