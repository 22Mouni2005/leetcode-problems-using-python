class Solution:
    def minOperations(self, s: str) -> int:
        res=0
        for i in s:
            if i=='a':
                continue
            moves=26-(ord(i)-97)
            res=max(res,moves)
        return res