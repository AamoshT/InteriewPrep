class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove the spacing, go through loop and one from first other from last
        #This would fail as there can be symbols and there can also be case sensi letters
        #chk = 'abcdefghijklmnopqrstuvwxyz1234567890'
        # = s.replace(" ","")
        #lcase = s.lower()
        #counter = 1
        #for i in range (len(s)):
        #    if s[i-1] in chk:
        #        if s[i-1]==s[-i]:
        #            counter+=1
        #        else:
        #            return False  
        #    else:
        #        counter +=1
        #return True
        nSt = ""
        for char in s:
            if char.isalnum():
                nSt += char.lower()
        return nSt == nSt[::-1]
