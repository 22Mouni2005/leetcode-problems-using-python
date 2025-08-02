class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[[1]]
        for i in range(1,rowIndex+1):
            l1=[]
            for j in range(i+1):
                if j==0 or j==i:
                    l1.append(1)
                else:
                    l1.append(l[i-1][j]+l[i-1][j-1])
            l.append(l1)
        return l[-1]
        