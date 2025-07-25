class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        h=len(height)-1
        maxi=0
        while l<h:
            if height[l]<=height[h]:
                maxi=max(maxi,height[l]*(h-l))
                l+=1
            else:
                maxi=max(maxi,height[h]*(h-l))
                h-=1
        return maxi