class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0], max(nums[:2])]

        for i in range(2, len(nums)):
            dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))

        return(dp[-1])