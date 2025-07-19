class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dup=[False]*(len(s)+1)
        dup[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dup[j] and s[j:i] in wordDict:
                    dup[i]=True
                    break
        return dup[-1]