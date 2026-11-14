class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        maxx = ""
        while i < len(s):
            # odd length
            l = i - 1
            r = i + 1
            currLength = 1
            currStr = s[i]
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    currLength = r - l + 1
                    currStr = s[l] + currStr + s[r]
                    r += 1
                    l -= 1
                else:
                    break
                

            if len(maxx) < currLength:
                maxx = currStr

            # even length
            l = i
            r = i + 1
            currLength = 0
            currStr = ""
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    currLength = r - l + 1
                    currStr = s[l] + currStr + s[r]
                    r += 1
                    l -= 1
                else:
                    break

            if len(maxx) < currLength:
                maxx = currStr
            
            i += 1

        return maxx