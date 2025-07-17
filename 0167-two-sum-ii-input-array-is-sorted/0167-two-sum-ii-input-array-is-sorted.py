class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        high=len(numbers)-1
        i=0
        while(i<high):
            if numbers[i]+numbers[high]==target:
                return [i+1,high+1]
            elif numbers[i]+numbers[high]<target:
                i=i+1
            else:
                high=high-1
        return []       