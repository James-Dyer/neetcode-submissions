func findDuplicate(nums []int) int {
    // loop thru nums
        // check for negativity
        
    for _, v := range nums {
        if v < 0 {
            v = -v
        }
        idx := v - 1
        if nums[idx] < 0 {
            return v
        }
        nums[idx] *= -1
    }

    return -1

}
