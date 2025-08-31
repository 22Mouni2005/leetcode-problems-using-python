class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=list(map(str,s.split(' ' or ',' or ':')))
        s1=""
        for i in s:
            if i.isalnum():
              s1+=i.lower()
        if s1==s1[::-1]:
            return True
        return False

        