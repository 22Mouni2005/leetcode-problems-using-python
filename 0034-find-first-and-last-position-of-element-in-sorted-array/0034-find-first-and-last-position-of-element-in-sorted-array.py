class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c=s=0
        l=[-1,-1]
        for i in range(len(nums)):
            if nums[i]==target and c==0:
                l[0]=l[1]=i
                c=c+1
            elif nums[i]==target:
                s=i
                c+=1
        if c>1:
            l[1]=s
        return l

        