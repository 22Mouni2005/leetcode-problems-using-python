class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        for i in range(1,n):
            new_s=""
            c=1
            for j in range(1,len(s)):
                if s[j]==s[j-1]:
                    c+=1
                else:
                    new_s+=str(c)+s[j-1]
                    c=1
            new_s+=str(c)+s[-1]
            s=new_s
        return s
        