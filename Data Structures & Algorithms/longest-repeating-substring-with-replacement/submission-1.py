# brute force: O(s^k)
# sliding window: contains distinct chars + at most k other chars -> O(n)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_window_size = 0
        left = 0
        max_freq = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            window_size = right - left + 1
            max_freq = max(max_freq, counts[s[right]])

            # a window is valid only if window_size <= most_freq_char + k
            while window_size > max_freq + k:
                # move left
                counts[s[left]] -= 1
                left += 1
                window_size = right - left + 1

            max_window_size = max(max_window_size, window_size)
            
            
        return max_window_size
                
