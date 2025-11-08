class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for word in strs:
            new=''.join(sorted(word))
            result[new].append(word)
        return list(result.values())
