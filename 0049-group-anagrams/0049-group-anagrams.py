class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        for i in strs:
            sort_word=''.join(sorted(i))
            anagram[sort_word].append(i)
        return list(anagram.values())
        