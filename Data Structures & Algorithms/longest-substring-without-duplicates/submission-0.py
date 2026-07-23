class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using set to make in 0(1) for removing item
        #two pointer 
        #sliding window, the window is l-r this will get updated ass the loop runs
        #keeping track of biggest window and returning that
        # space 0(n) time 0(n)
        charSet = set()
        l=0
        res =0
        for r in range (len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max(res,r-l+1)
        return res


        