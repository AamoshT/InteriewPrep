class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        val = []
        # have three pointers that can indivially go through a list
        # might need to sort them (nt sure if this is goood for interview)
        #there run three pointer one from start two from end and end+1
        #
        nums.sort()
        for i,vall in enumerate (nums):
            if i > 0 and vall == nums[i-1]:
                continue
            ptrOne = i+1
            ptrTwo = len(nums)-1
            while ptrOne < ptrTwo:
                sum = vall + nums[ptrOne] + nums[ptrTwo]
                if sum > 0:
                    ptrTwo -= 1
                elif sum < 0:
                    ptrOne += 1
                else:
                    val.append([vall, nums[ptrOne], nums[ptrTwo]])
                    ptrOne += 1
                    while nums[ptrOne] == nums[ptrOne-1] and ptrOne < ptrTwo:
                        ptrOne += 1
        return val