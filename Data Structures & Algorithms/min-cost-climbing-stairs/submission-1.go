func minCostClimbingStairs(cost []int) int {
	prev1, prev2 := 0, 0

	for i := 2; i <= len(cost); i++ {
		temp := prev1
		prev1 = min(prev1+cost[i-1], prev2+cost[i-2])
		prev2 = temp
	}

	return prev1
}
