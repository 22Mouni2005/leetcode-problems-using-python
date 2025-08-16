class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=[]
        maxi=0
        c=0
        for i in range(len(s)):
            if s[i] not in s1:
                s1.append(s[i])
                c+=1
                maxi=max(maxi,c)
            else:
                c=0
                s1.clear()
        return maxi