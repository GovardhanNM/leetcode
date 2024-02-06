class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [n - 1] * n

        maxi = height[0]
        max_index = 0
        for i in range(n):
            if height[i] > maxi:
                maxi = height[i]
                max_index = i
            left_max[i] = max_index

        maxi = height[-1]
        max_index = n - 1
        for i in range(n - 1, -1, -1):
            if height[i] > maxi:
                maxi = height[i]
                max_index = i
            right_max[i] = max_index
        # print(left_max, right_max)

        ans = 0
        for i in range(1, n - 1):
            curr = min(height[left_max[i]], height[right_max[i]]) - height[i]
            ans += curr
            # print(curr)
        return ans
