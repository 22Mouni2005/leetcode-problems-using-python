class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[0]*n
        b=[0]*n
        a[0]=0
        b[n-1]=0
        for i in range(1,n):
            a[i]=a[i-1]+nums[i-1]
        for i in range(n-2,-1,-1):
            b[i]=b[i+1]+nums[i+1]
        res=[0]*n
        for i in range(n):
            if b[i]-a[i] >=0:
                res[i]=b[i]-a[i]
            else:
                res[i]=a[i]-b[i]
        return res
        