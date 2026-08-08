class Solution:
    def reverseBits(self, n: int) -> int:
        # take the last bit of n
        # add to my result on the left side
        # shift n to the right
        # repeat 32 times

        result = 0

        for i in range (32):
            bit = n & 1
            result = (result << 1) | bit
            n >>= 1

        return result