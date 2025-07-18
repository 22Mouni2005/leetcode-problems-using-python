class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix)-1
        while low<=high:
            mid=(low+high)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                if target in matrix[mid]:
                    return True
                low=mid+1
            elif matrix[mid][0]>target:
                high=mid-1
        return False