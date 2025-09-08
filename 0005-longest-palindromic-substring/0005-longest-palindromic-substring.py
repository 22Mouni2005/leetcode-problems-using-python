class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1 or s==s[::-1]:
            return s
        n=len(s)
        res=""
        l=0
        r=n-1
        maxi=float('-inf')
        while l<n-1:
            if l==r:
                l=l+1
                r=n-1
            s1=s[l:r+1]
            if s1==s1[::-1] and maxi<len(s1):
                maxi=len(s1)
                res=s1
            r-=1
        return res
        