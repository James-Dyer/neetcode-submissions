class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force is O(n^2), simulate starting at each idx from 0..n
        
        # my solution: calculate gas - cost differences for each idx, start at biggest difference.
        # O(n)
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start
