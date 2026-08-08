class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		queue = deque()
		m, n = len(grid), len(grid[0])
		healthy = 0

		# append all pos of rotten fruit to queue
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 2:
					queue.append((i, j))
				elif grid[i][j] == 1:
					healthy += 1

		if healthy == 0:
			return 0

		minutes = -1
		while queue:
			level_size = len(queue)
			minutes += 1

			for _ in range(level_size):
				# process fruit
				x, y = queue.popleft()
				directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
				for dx, dy in directions:
					nx, ny = x + dx, y + dy

					if (
						0 <= nx < m 
						and 0 <= ny < n
						and grid[nx][ny] == 1
					):
						queue.append((nx, ny))
						grid[nx][ny] = 2
						healthy -= 1
		
		return minutes if not healthy else -1
