class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=[]
        m=[]
        a=list(set(arr))
        for i in range(len(a)):
            s=arr.count(a[i])
            l.append(s)
        for j in range(len(l)):
            if l[j]==a[j]:
                m.append(a[j])
        if len(m)==0:
            return -1
        return max(m)
