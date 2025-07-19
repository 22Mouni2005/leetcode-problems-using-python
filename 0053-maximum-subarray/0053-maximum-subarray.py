class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_glob=m_curr=nums[0]
        for num in nums[1:]:
            m_curr=max(num,m_curr+num)
            m_glob=max(m_curr,m_glob)
        return m_glob


        