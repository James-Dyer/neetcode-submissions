func climbStairs(n int) int {
    // stair[i] = stair[i-1] + stair[i-2]
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}

	prev2, prev1 := 1, 2
	//prev2 = n-2, prev1 = n-1

	for i := 3; i <= n; i++ {
		curr := prev1 + prev2
		prev2 = prev1
		prev1 = curr
	}

	return prev1
}
