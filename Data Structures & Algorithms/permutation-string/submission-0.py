class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        l = 0
        for r in range(len(s2)):
            freq[s2[r]] = freq.get(s2[r], 0) - 1
            if freq[s2[r]] == 0:
                del freq[s2[r]]
            if freq == {}:
                return True
            while min(freq.values()) < 0 and l < r:
                freq[s2[l]] = freq.get(s2[l], 0) + 1
                if freq[s2[l]] == 0:
                    del freq[s2[l]]
                l += 1
        return False
