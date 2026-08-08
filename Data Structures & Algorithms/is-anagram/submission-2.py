class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # frequency array
        arr = [0] * 26

        # populate freq arr with s
        for letter in s:
            temp = ord(letter) - ord('a')
            arr[temp] += 1
        # depopulate freq arr with t
        for letter in t:
            temp = ord(letter) - ord('a')
            arr[temp] -= 1
        # check to see if array is empty 
        for bucket in arr:
            if bucket != 0:
                return False
        
        return True
        # O(n)


       