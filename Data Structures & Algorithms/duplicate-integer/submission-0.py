class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i, vals in enumerate(nums):
            if i == (len(nums)-1):
                return False
            if nums[i] == nums[i+1]:
                return True