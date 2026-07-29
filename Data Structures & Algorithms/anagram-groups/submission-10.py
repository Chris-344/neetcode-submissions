class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj=defaultdict(list)
        for i in strs:
            charArr=[0]*26
            for j in i:
                charArr[ord(j)-ord("a")]+=1
            obj[tuple(charArr)].append(i)
        return list(obj.values())