class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c=0
        cur_c=0
        for i in nums:
            if i==1:
                cur_c+=1
                max_c=max(max_c,cur_c)
            else:
                cur_c=0
        return max_c

        