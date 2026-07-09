class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=0
        y=n
        l=[]
        for i in range(n):
            l.append(nums[i+x])
            l.append(nums[y+i])
        return l
        