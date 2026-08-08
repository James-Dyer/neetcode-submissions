func lengthOfLongestSubstring(s string) int {
    // sliding window with seen dict
    // 's' -> last seen index
    // when we see a duplicate, we move the left pointer to the last seen index + 1 and update

    var left int
    var max_substring int
    seen := make(map[byte]int)
    for right := 0; right < len(s); right++ {
        if idx, ok := seen[s[right]]; ok {
            for left <= idx {
                delete(seen, s[left])
                left++
            }
        } 
        max_substring = max(max_substring, right-left+1)
        seen[s[right]] = right
    }

    return max_substring
}
