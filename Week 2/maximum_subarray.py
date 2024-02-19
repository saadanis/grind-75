class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -100000
        current = 0

        for num in nums:
            current = max(num, current + num)
            maximum = max(maximum, current)

        return maximum