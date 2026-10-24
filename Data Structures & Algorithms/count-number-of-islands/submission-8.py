class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        islands = 0

        def is_valid(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

        def dfs(i, j):
            if not is_valid(i, j) or grid[i][j] != '1':
                return

            grid[i][j] = '0'
            for dirr in dirs:
                dfs(i + dirr[0], j + dirr[1])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        

        return islands