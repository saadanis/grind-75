class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        
        ways  = [1,2] + [-1] * (n-2) # TIL, pre-assignment is a little faster than appending, maybe.

        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[-1]