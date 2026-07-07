class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n=str(n)
        x=0
        sum=0
        for i in n:
            if i=='0':
                continue
            x=x*10+int(i)
            sum+=int(i)
        return x*sum
        