class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst,mapts={},{}
        for i in range(len(s)):
            chars,chart=s[i],t[i]
            if chars in mapst and mapst[chars]!=chart:
                return False
            if chart in mapts and mapts[chart]!=chars:
                return False
            mapst[chars]=chart
            mapts[chart]=chars
        return True
        