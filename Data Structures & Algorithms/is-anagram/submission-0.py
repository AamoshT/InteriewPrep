class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1,c2={},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            c1[s[i]] = 1 + c1.get(s[i],0)
            c2[t[i]] = 1 + c2.get(t[i],0)
        for c in c1:
            if c1[c] !=c2.get(c,0):
                return False
        return True
           
