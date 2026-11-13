class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRS = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(x, y, count):
            if grid[x][y] == 1:
                count += 1
                grid[x][y] = -1

                for d in DIRS:
                    newx, newy = x + d[0], y + d[1]

                    if 0 <= newx < ROWS and 0 <= newy < COLS:
                        count = dfs(newx, newy, count)

            return count

        maxx = -1
        for i in range(ROWS):
            for j in range(COLS):
                temp = 0
                temp = dfs(i, j, temp)
                maxx = max(maxx, temp)

        
        return maxx

