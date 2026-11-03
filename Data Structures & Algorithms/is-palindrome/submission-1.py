class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum()).lower()
        print(cleaned)
        for i in range(0, len(cleaned)//2):
            if cleaned[i] != cleaned[-i-1]:
                return False
        return True