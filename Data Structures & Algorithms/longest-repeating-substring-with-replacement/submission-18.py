from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxLength = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            mostFreq = max(freq.values())
            if (r - l + 1) - mostFreq <= k:
                maxLength = max(maxLength, r - l + 1)
                print("maxlength", maxLength, "r and l", r, l, "r - l + 1 and k", r - l + 1, k)
            else:
                freq[s[l]] -= 1
                l += 1
        return maxLength


