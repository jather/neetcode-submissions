class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            digits = ""
            while s[i] != "#":
                digits += s[i]
                i += 1
            i += 1
            length = int(digits)
            decoded.append(s[i:i+ length])
            i += length
        return decoded 
