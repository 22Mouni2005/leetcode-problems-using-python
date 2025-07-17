class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    l.append(i)
                    l.append(j)
                    c+=1
            if c==1:
                break      
        return l
        