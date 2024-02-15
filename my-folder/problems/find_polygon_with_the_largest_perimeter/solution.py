class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        prefix_sum = nums[0]

        # print(nums, prefix_sum)
        ans = -1
        for i in range(2, n):
            prefix_sum += nums[i - 1]
            if prefix_sum > nums[i]:
                ans = max(ans, prefix_sum + nums[i])

        return ans
