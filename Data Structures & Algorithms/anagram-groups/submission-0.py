class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            letters = [0] * 26
            for letter in word:
                letters[ord(letter) - ord("a")] += 1
            key = tuple(letters)
            dictionary[key] = dictionary.get(key, [])
            dictionary[key].append(word)

        return [dictionary[key] for key in dictionary]
