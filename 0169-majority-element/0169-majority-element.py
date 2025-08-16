class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        m=0
        ma=0
        s=list(set(nums))
        for i in s:
            if nums.count(i)>ma:
                ma=nums.count(i)
                m=i
        return m

        