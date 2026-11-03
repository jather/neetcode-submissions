class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lettersS, lettersT = {}, {}
        for i in range(0,len(s)):
            lettersS[s[i]] = 1 + lettersS.get(s[i], 0)
            lettersT[t[i]] = 1 + lettersT.get(t[i], 0)
        return lettersS == lettersT