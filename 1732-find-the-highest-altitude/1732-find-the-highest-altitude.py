class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[0]*(len(gain)+1)
        for i in range(0,len(gain)):
            l[i+1]=gain[i]+l[i]
        return max(l)
        