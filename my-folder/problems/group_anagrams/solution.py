class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for word in strs:
            num = [0] * 26
            for letter in word:
                index = (ord(letter) - ord('a'))
                num[index] += 1
            key = tuple(num)
            if key not in cache:
                cache[key] = []
            cache[key].append(word)

        return cache.values()
        