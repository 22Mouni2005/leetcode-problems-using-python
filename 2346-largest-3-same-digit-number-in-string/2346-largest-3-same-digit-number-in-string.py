class Solution:
    def largestGoodInteger(self, num: str) -> str:
        c=0
        val=""
        maxi=-1
        if len(num)==3 and num.count(num[0])==3:
            val=num
        else:
            if num[-1]==num[-2] and num[-2]==num[-3]:
                maxi=int(num[-1])
                val=num[-3:]
            for i in range(len(num)-3):
                if num[i]==num[i+1] and num[i+1]==num[i+2] and int(num[i])>maxi:
                    maxi=int(num[i])
                    val=num[i:i+3]
        return val