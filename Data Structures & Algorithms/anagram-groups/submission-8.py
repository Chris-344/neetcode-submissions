class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            letters=[0]*26
            for k in i:
                letters[ord(k)-ord("a")]+=1
            res[tuple(letters)].append(i)
        return list(res.values())