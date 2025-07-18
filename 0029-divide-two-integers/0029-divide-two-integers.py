class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=dividend/divisor
        if divisor==-1 and dividend==-2147483648:
            return int(res-1)
        return int(res)
        