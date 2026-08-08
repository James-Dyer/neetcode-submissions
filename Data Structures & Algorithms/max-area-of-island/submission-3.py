class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		max_size = 0
		visited = set()
		n, m = len(grid), len(grid[0])
		
		def size_of_island(x, y) -> int:
			if (x, y) in visited:
				return 0
			visited.add((x, y))
			area = 1
			
			if x > 0 and grid[x - 1][y] == 1:
				area += size_of_island(x - 1, y)
			if x < n - 1 and grid[x + 1][y] == 1:
				area += size_of_island(x + 1, y)
			if y > 0 and grid[x][y - 1] == 1:
				area += size_of_island(x, y - 1)
			if y < m - 1 and grid[x][y + 1] == 1:
				area += size_of_island(x, y + 1)

			return area
			

		for i in range(n):
			for j in range(m):
				if grid[i][j] == 1 and (i, j) not in visited:
					max_size = max(max_size, size_of_island(i, j))
		
		return max_size
