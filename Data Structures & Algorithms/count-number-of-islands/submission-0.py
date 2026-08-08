class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate thru the grid
        # when we see a 1
            

        seen = set()
        count = 0
        stack = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    count += 1
                    stack.append((i, j))
                    while stack:
                        x, y = stack.pop()
                        if grid[x][y] == "1":
                            seen.add((x, y))
                            if x + 1 < len(grid) and (x + 1, y) not in seen:
                                stack.append((x + 1, y))
                            if x - 1 >= 0 and (x - 1, y) not in seen:
                                stack.append((x - 1, y))
                            if y + 1 < len(grid[x]) and (x, y + 1) not in seen:
                                stack.append((x, y + 1))
                            if y - 1 >= 0 and (x, y - 1) not in seen:
                                stack.append((x, y - 1))

                    # add surrounding spaces to stack
        
        return count

