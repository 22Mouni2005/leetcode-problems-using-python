class Solution:
    def sortVowels(self, s: str) -> str:
        l=[]
        index=[]
        s1=[]
        flag=-1
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                l.append(s[i])
        l.sort()
        j=0
        for c in s:
            if c in 'aeiouAEIOU':
                s1.append(l[j])
                j+=1
            else:
                s1.append(c)
        return "".join(s1)
