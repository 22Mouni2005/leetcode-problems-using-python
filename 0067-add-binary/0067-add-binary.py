class Solution:
    def addBinary(self, a: str, b: str) -> str:
        asum=0
        s=""
        bs=0
        j=0
        for i in range(len(a)-1,-1,-1):
            asum+=(int(a[i])*(2**j))
            j+=1
        j=0
        for i in range(len(b)-1,-1,-1):
            bs+=(int(b[i])*(2**j))
            j+=1
        res=asum+bs
        if res==0:
            return "0"
        while res>=2:
            r=res%2
            s+=str(r)
            res=res//2
        if res==1:
            s+="1"
        return s[::-1]