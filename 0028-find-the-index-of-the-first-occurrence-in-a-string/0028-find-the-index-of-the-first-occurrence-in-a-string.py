class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s=-1
        if needle in haystack:
            for j in range(len(haystack)):
                if needle[:] == haystack[j:j+len(needle)]:
                    s=j
                    break
        if s!=-1:
            return s
        else:
            return -1