class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        islands = 0

        def is_valid(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])


        def dfs(i, j):
            if not is_valid(i, j) or grid[i][j] == "0":
                return

            visited.add((i, j))

            for dirr in dirs:
                newi = dirr[0] + i
                newj = dirr[1] + j


                if (newi, newj) not in visited:
                    
                    dfs(newi, newj)

            
            

        for n in range(len(grid)):
            for m in range(len(grid[n])):
                if grid[n][m] == "1" and (n, m) not in visited:

                    islands += 1
                    dfs(n, m)

        return islands