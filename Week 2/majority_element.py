class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
        
# There's tons of ways to do this easily. This is simply one of many.