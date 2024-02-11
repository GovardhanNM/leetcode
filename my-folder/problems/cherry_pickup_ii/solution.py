class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.points = [[1, -1], [1, 0], [1, 1]]
        cache = {}

        def is_valid(x, y):
            return x >= 0 and x < self.m and y >= 0 and y < self.n

        def find_ans(x1, y1, x2, y2):
            ans = 0

            valid_1 = is_valid(x1, y1)
            valid_2 = is_valid(x2, y2)
            if not valid_1 and not valid_2:
                return ans

            if (x1, y1, x2, y2) in cache:
                return cache[(x1, y1, x2, y2)]

            if valid_1 and valid_2 and x1 == x2 and y1 == y2:
                ans += grid[x1][y1]
            else:
                if valid_1:
                    ans += grid[x1][y1]

                if valid_2:
                    ans += grid[x2][y2]

            maxi = 0
            for point1 in self.points:
                for point2 in self.points:
                    maxi = max(maxi, find_ans(x1 + point1[0], y1 + point1[1], x2 + point2[0], y2 + point2[1]))

            cache[(x1, y1, x2, y2)] = (ans + maxi)
            return ans + maxi

        return find_ans(0, 0, 0, self.n - 1)

            
