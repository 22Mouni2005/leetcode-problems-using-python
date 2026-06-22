class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        for i in text:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return min(
            d.get('b',0),
            d.get('a',0),
            d.get('l',0)//2,
            d.get('o',0) //2,
            d.get('n',0)
        )
        
        