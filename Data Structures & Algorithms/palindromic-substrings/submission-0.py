class Solution:
    def countSubstrings(self, s: str) -> int:
        i = 0
        total = 0
        while i < len(s):
            # odd length
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    r += 1
                    l -= 1
                    total += 1
                else:
                    break

            # even length
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    r += 1
                    l -= 1
                    total += 1
                else:
                    break
            
            i += 1

        return total