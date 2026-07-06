class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxi=float('-inf')
        start=0
        def is_pal(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        for i in range(n):
            for j in range(i,n):
                if is_pal(i,j):
                    l=j-i+1
                    if l>maxi:
                        maxi=l
                        start=i
        return s[start:start+maxi]
        