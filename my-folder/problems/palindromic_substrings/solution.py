class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(n):
            a = i
            b = i

            while a >= 0 and b < n and s[a] == s[b]:
                ans += 1
                a -= 1
                b += 1

            a = i
            b = i + 1

            while a >= 0 and b < n and s[a] == s[b]:
                ans += 1
                a -= 1
                b += 1

        return ans
        