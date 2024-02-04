class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        ans = ceil(n / k)
        
        for i in range(k, n, k):
            j = i
            temp = 0
            flag = True
            while j < n:
                if word[temp] != word[j]:
                    flag = False
                    break
                temp += 1
                j += 1
            if flag:
                ans = min(ans, i//k)
                break
        
        return ans