func subsets(nums []int) [][]int {
    n := len(nums)
	res := make([][]int, 0, 1<<n)
    subset := make([]int, 0, n)
    var dfs func(int)

    dfs = func(i int) {
        if i >= n {
            tmp := make([]int, len(subset))
            copy(tmp, subset)
            res = append(res, tmp)
            return
        }

        subset = append(subset, nums[i])
        dfs(i + 1)

        subset = subset[:len(subset)-1]
        dfs(i + 1)
    }

    dfs(0)
    return res

}
