class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, 101):
            squares.append(i * i)

        cache = {}
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == math.isqrt(i) ** 2:
                dp[i] = 1
                continue

            dp[i] = i

            for j in range(1, 100):
                rem = i - (j * j)
                if rem > 0:
                    dp[i] = min(dp[i], 1 + dp[rem])
                else:
                    break

        # print(dp)
        return dp[n]