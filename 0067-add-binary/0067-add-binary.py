class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=0
        for i in digits:
            s=s*10+i
        s=s+1
        l=[]
        while s>0:
            l.insert(0,s%10)
            s=s//10
        return l
        