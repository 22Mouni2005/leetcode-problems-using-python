class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=[]
        for i in range(n//2):
            l.append(i+1)
            l.append(-(i+1))
        if n%2:
            l.append(0)
        return l
        