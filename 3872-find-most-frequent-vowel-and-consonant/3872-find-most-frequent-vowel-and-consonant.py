class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_v=0
        max_c=0
        for i in s:
            if i in 'aeiou' and s.count(i)>max_v:
                max_v=s.count(i)
            elif i not in "aeiou" and s.count(i)>max_c:
                max_c=s.count(i)
        return max_v+max_c

        