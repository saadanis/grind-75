class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]