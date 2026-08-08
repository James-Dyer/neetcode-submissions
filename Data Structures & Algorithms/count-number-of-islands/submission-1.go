func numIslands(grid [][]byte) int {
	seen := make(map[[2]int]struct{})
	count := 0

	for i, row := range grid {
		for j, tile := range row {

			if _, exists := seen[[2]int{i, j}]; exists || tile != '1' {
				continue
			}

			count++

			// use slice as stack
			stack := [][2]int{{i, j}}

			for len(stack) > 0 {
				// pop
				curr := stack[len(stack)-1]
				stack = stack[:len(stack)-1]

				x, y := curr[0], curr[1]

				if x < 0 || x >= len(grid) ||
					y < 0 || y >= len(grid[x]) {
					continue
				}

				if grid[x][y] != '1' {
					continue
				}

				pos := [2]int{x, y}

				if _, exists := seen[pos]; exists {
					continue
				}

				seen[pos] = struct{}{}

				// push neighbors
				stack = append(stack,
					[2]int{x + 1, y},
					[2]int{x - 1, y},
					[2]int{x, y + 1},
					[2]int{x, y - 1},
				)
			}
		}
	}

	return count
}