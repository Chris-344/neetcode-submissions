class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap=defaultdict(list)
        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            countMap[tuple(count)].append(s)

        return [x for x in countMap.values()]