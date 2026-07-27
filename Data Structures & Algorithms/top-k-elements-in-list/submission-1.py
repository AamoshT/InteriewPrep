class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        while k > 0:
            key = max(count, key=count.get)  
            res.append(key)
            count.pop(key)
            k -= 1

        return res