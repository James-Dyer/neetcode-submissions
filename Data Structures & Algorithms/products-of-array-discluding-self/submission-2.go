func productExceptSelf(nums []int) []int {

	n := len(nums) 
	prefix := make([]int, n, n)
	suffix := make([]int, n, n)
	prefix[0] = 1
	suffix[n-1] = 1
	for i := 1; i < n; i++ {
		prefix[i] = prefix[i-1] * nums[i-1]
		suffix[n-i-1] = suffix[n-i] * nums[n-i]
	}

	res := make([]int, n, n)
	for i := 0; i < n; i++ {
		res[i] = prefix[i] * suffix[i]
	}

	// at nums[i], res = prefix[i] * suffix[i]
	return res
}
