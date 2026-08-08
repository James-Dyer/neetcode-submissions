func search(nums []int, target int) int {
    var left, right int = 0, len(nums)-1

    for left <= right {
        // calculate center
        center := left + (right - left) / 2
        // if target is larger, then left = center
        if target > nums[center] {
            left = center + 1
        } else if target < nums[center] {
            right = center - 1
        } else {
            return center
        }
        // if target is smaller, then right = center
        // if center == target return center
    }

    return -1

    // O(logn)
}
