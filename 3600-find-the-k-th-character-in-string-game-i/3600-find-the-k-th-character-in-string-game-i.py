class Solution:
    def kthCharacter(self, k: int) -> str:
        s="a"
        while len(s)<=k:
            s1 = "".join(chr(ord(c) + 1) for c in s)
            s=s+s1
        return s[k-1]   