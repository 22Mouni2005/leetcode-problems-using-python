class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            c=0
            for j in nums:
                if i==j:
                    c+=1
                if c>1:
                    break
            if c==1:
                return i