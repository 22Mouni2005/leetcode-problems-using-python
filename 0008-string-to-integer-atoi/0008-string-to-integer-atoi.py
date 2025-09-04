class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s :
            return 0
        sign=1
        if s[0] in ['+','-']:
            if s[0]=='-':
                sign=-1
            s=s[1:]
        res=0
        for i in s:
            if not i.isdigit():
                break
            res=res*10+int(i)
        res=res*sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res

        