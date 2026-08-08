class Solution:
	def islandsAndTreasure(self, grid: List[List[int]]) -> None:
		queue = deque()
		m, n = len(grid), len(grid[0])

		# append treasure chest coords to queue
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 0:
					queue.append((i, j, 0))

		while queue:
			x, y, level = queue.popleft()
			if grid[x][y] == 2147483647:
				grid[x][y] = level
			
			if grid[x][y] != -1:
				if x > 0 and (x - 1, y) and grid[x - 1][y] == 2147483647:
					queue.append((x - 1, y, level + 1))
				if x < m - 1 and grid[x + 1][y] == 2147483647:
					queue.append((x + 1, y, level + 1))
				if y > 0 and grid[x][y - 1] == 2147483647:
					queue.append((x, y - 1, level + 1))
				if y < n - 1 and grid[x][y + 1] == 2147483647:
					queue.append((x, y + 1, level + 1))