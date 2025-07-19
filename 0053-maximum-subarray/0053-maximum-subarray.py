class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_glob=m_curr=nums[0]
        for i in range(1,len(nums)):
            m_curr=max(nums[i],m_curr+nums[i])
            m_glob=max(m_curr,m_glob)
        return m_glob


        