class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[n-1] is <9, increment and return
        # else while i = n-1 is 9 and i >= 0, set 0 and i--

        n = len(digits) - 1
        if digits[n] < 9:
            digits[n] = digits[n] + 1
            return digits
        else:
            i = n
            while i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                    i -= 1
                else:
                    digits[i] = digits[i] + 1
                    return digits

            if i == -1: 
                digits.insert(0, 1)
        
        return digits
