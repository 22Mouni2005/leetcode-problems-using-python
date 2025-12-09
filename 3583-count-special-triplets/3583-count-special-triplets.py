from collections import Counter, defaultdict
MOD=10**9+7
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        suffix = Counter(nums)     # counts of all numbers on the right
        prefix = defaultdict(int)  # counts of numbers on the left
        
        count = 0
        
        for i, x in enumerate(nums):
            suffix[x] -= 1         # current element is no longer in right side
            
            m = x * 2              # the target value
            
            if prefix[m] > 0 and suffix[m] > 0:
                count += prefix[m] * suffix[m]
                
            prefix[x] += 1         # add current value to left side
        
        return count%MOD
