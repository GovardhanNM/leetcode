class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        keys = list(counter.values())
        keys.sort()

        rem = len(keys)

        for i in range(len(keys)):
            k -= keys[i]
            if k < 0:
                break
            rem -= 1
            
        return rem