func findDuplicate(nums []int) int {
    seen := make(map[int]struct{})

    for _, v := range nums {
        if _, ok := seen[v]; ok {
            return v
        }
        seen[v] = struct{}{}
    }

    return -1

}
