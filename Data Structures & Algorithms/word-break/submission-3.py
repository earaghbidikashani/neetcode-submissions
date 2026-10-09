class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        neverWorks = set()
        def check(index):
            if index == len(s):
                return True
            
            if index in neverWorks:
                return False

            for word in wordDict:
                currWord = s[index:index + len(word)]
                if currWord == word:
                    checked = check(index + len(word))
                    if checked:
                        return True

            neverWorks.add(index)

            return False
        return check(0)

