class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #check one and go to next and repeat
        # have two pointer one in the start and one at the end then decrese
        # the one at the end when the sum is bigger than targert increse the one the front
        #when the sum is smaller
        ptrOne = 0
        ptrTwo = len(numbers)-1
        for i in range (len(numbers)):
            ttl = numbers[ptrOne]+numbers[ptrTwo]
            if ttl > target:
                ptrTwo -= 1
            elif ttl < target:
                ptrOne += 1
            else:
                return list ((ptrOne+1,ptrTwo+1))
