func topKFrequent(nums []int, k int) []int {
    // build a freq map
	freq_map := make(map[int]int)
	for _, v := range nums {
		freq_map[v] += 1
	}

	// add them all to a slice
	arr := make([][2]int, 0, len(nums))
	for num, freq := range freq_map {
		arr = append(arr, [2]int{freq, num})
	}

	// sort slice
	sort.Slice(arr, func(i, j int) bool {
		return arr[i][0] > arr[j][0]
	})

	// return the bottom k elements
	res := make([]int, 0, k)
	for i := 0; i < k; i++ {
		res = append(res, arr[i][1])
	}
	return res
}
