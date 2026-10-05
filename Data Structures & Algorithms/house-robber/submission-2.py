class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        i = 1
        while i < len(nums):
            if i > 1:
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            else:
                dp[i] = max(nums[i], dp[i - 1])

            i += 1

        return dp[-1]