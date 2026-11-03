class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) - 1
        l = 0
        shortest = None
        for r, c in enumerate(s):
            if c in freq:
                freq[c] += 1
            while (min(freq.values()) >= 0) and l <= r:
                if shortest is None or shortest[1] - shortest[0] > r - l:
                    shortest = (l, r)
                if s[l] in freq:
                    freq[s[l]] -= 1
                l += 1
        if shortest is None:
            return ""
        return s[shortest[0]:shortest[1] + 1]
            
        