class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l=[]
        for a in range(1,n):
            if '0' not in str(a) and '0' not in str(n-a):
                l.append(a)
                l.append(n-a)
                break
        return l
        