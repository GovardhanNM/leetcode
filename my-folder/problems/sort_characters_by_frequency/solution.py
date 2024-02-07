class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        s = list(s)
        
        s.sort(key=lambda x: (-counter[x], ord(x)))

        return ''.join(s)