class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #brute force - we can iterate through every single item and check every single occurance and return when satified
       #Time - O(2^n) Space - 0(1) 
       #Edge cases can be empty, are these in order like sorted?
       prevMap ={} #store prev element
       for i ,val in enumerate (nums):
        diff = target-val
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[val] = i