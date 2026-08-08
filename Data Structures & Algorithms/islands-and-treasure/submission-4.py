class Solution:
	def islandsAndTreasure(self, grid: List[List[int]]) -> None:
		queue = deque()
		m, n = len(grid), len(grid[0])

		# append treasure chest coords to queue
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 0:
					queue.append((i, j))

		while queue:
			x, y = queue.popleft()
			
			if x > 0 and grid[x - 1][y] == 2147483647:
				grid[x - 1][y] = grid[x][y] + 1
				queue.append((x - 1, y))
			if x < m - 1 and grid[x + 1][y] == 2147483647:
				grid[x + 1][y] = grid[x][y] + 1
				queue.append((x + 1, y))
			if y > 0 and grid[x][y - 1] == 2147483647:
				grid[x][y - 1] = grid[x][y] + 1
				queue.append((x, y - 1))
			if y < n - 1 and grid[x][y + 1] == 2147483647:
				grid[x][y + 1] = grid[x][y] + 1
				queue.append((x, y + 1))