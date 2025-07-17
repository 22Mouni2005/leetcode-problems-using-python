class Solution:
    def reverse(self, x: int) -> int:
        r=0
        flag=1
        if x>=0:
            flag=1
        else:
            x=-x
            flag=0
        while x!=0:
            r=r*10+x%10
            x=x//10
        if flag==0:
            r=-r
        if r> 2**31 -1 or r< -2**31:
            return 0
        return r

