class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for ele in strs:
            arr=[0]*26
            for i in ele:
                arr[ord(i)-ord('a')]+=1
            res[tuple(arr)].append(ele)
        return list(res.values())