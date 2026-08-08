class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		n, m = len(grid), len(grid[0])
		count = 0

		visited = set()

		def explore_island(x, y) -> None:
			if (x,y) in visited:
				return
			
			visited.add((x,y))

			if x > 0 and grid[x - 1][y] == "1":
				explore_island(x - 1, y)
			
			if x < n - 1 and grid[x + 1][y] == "1":
				explore_island(x + 1, y)

			if y > 0 and grid[x][y - 1] == "1":
				explore_island(x, y - 1)

			if y < m - 1 and grid[x][y + 1] == "1":
				explore_island(x, y + 1)

        
		for i in range(n):
			for j in range(m):
				if grid[i][j] == "1" and (i, j) not in visited:
					count += 1
					explore_island(i, j)
		
		return count

