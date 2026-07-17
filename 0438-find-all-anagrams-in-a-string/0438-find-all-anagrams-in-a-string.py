class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        target = {}
        window = {}

        # Frequency of p
        for ch in p:
            target[ch] = target.get(ch, 0) + 1

        # First window
        for ch in s[:len(p)]:
            window[ch] = window.get(ch, 0) + 1

        ans = []

        if window == target:
            ans.append(0)

        for i in range(len(p), len(s)):

            # Add new character
            window[s[i]] = window.get(s[i], 0) + 1

            # Remove left character
            left = s[i - len(p)]
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            if window == target:
                ans.append(i - len(p) + 1)

        return ans

        