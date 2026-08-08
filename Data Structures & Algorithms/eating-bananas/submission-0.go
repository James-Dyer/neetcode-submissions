import "slices"

func hoursNeeded(piles []int, k int) int {
	hours := 0

	for _, pile := range piles {
		hours += (pile + k - 1) / k
	}

	return hours
}


func minEatingSpeed(piles []int, h int) int {
	// upper bound k = max(piles)
	// lower bound 1
	var answer int
	slices.Sort(piles[:])
	var left, right int = 1, piles[len(piles)-1]
	for left <= right {
		k := left + (right-left)/2
    	hours := hoursNeeded(piles, k)

		if hours <= h {
			answer = k
			right = k - 1
		} else {
			left = k + 1
		}
	}

	return answer
}
