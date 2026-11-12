class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        maxx = 0

        for r, char in enumerate(s):
            if char in last_seen:
                l = max(l, last_seen[char] + 1)

            last_seen[char] = r
            maxx = max(maxx, r - l + 1)

        return maxx