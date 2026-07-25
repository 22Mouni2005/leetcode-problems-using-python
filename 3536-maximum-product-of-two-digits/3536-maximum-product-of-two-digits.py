class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        while n:
            l.append(n%10)
            n//=10
        l.sort()
        return l[-1]*l[-2]
        