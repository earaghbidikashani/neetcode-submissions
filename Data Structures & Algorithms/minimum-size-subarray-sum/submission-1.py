class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        t = 0
        minn = float("inf")

        for r in range(len(nums)):
            t += nums[r]
            print("")
            print(t)
            
            while t >= target and l <= r:
                minn = min(minn, r - l + 1)
                t -= nums[l]
                l += 1
                
                

            print(l)
            print(r)
            print(minn)

        return 0 if minn == float("inf") else minn
