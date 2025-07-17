class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings=sorted(meetings)
        r,c=[0]*n,[0]*n
        for s,e in meetings:
            found=0
            for i,f in enumerate(r):
                if f<=s:
                    r[i]=e
                    c[i]+=1
                    found=1
                    break
            if not found:
                j=r.index(min(r))
                r[j]+=e-s
                c[j]+=1
        return c.index(max(c))
        