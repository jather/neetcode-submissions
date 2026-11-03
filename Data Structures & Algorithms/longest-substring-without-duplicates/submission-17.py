class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        longest = 0
        for i in range(0, len(s)):
            if s[i] in seen:
                l = max(l, seen[s[i]] + 1)
            seen[s[i]] = i
            longest = max(longest, i - l + 1)
        return longest

            
