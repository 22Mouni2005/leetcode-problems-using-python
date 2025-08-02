class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(numRows):
            l1=[]
            for j in range(i+1):
                if j==0 or i==j:
                    l1.append(1)
                else:
                    l1.append(l[i-1][j]+l[i-1][j-1])
            l.append(l1)
        return l

        