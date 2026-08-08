class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        myDict = dict()

        for char in s:
            if char in myDict:
                myDict[char] = myDict[char] + 1
            else:
                myDict[char] = 1

        for char in t:
            if char in myDict and myDict[char] >= 1:
                myDict[char] = myDict[char] - 1
            else:
                return False
        
        return True
