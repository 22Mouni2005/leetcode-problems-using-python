class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        maxs=""
        for i in range(len(strs[0])):
            c=strs[0][i]
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=c:
                    return maxs
            maxs+=c
        return maxs
            

        