from collections import defaultdict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dictt = defaultdict(int) # input : longest

        for num in nums:
            maxx = -1
            for dic in dictt.keys():
                if dic < num:
                    maxx = max(maxx, dictt[dic] + 1)
            if maxx == -1: 
                maxx = 1
            dictt[num] = max(dictt[num], maxx)

        print(dictt)
        return max(dictt.values())

                