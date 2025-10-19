# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def num(i,n):
            mid=(n+i)//2
            if guess(mid)==0:
                return mid
            if guess(mid)==-1:
                return num(i,mid-1)
            else:
                return num(mid+1,n)
        return num(1,n)




















































        