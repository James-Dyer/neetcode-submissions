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
			
			directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
			for dx, dy in directions:
				nx, ny = x + dx, y + dy

				if (
					0 <= nx < m
					and 0 <= ny < n
					and grid[nx][ny] == 2147483647
				):
					grid[nx][ny] = grid[x][y] + 1
					queue.append((nx, ny))