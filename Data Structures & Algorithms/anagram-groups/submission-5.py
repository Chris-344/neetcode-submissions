class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        obj=defaultdict(list)
        for s in strs:
                arr=[0]*26
                for i in s:
                        arr[ord(i)-ord("a")]+=1
                obj[tuple(arr)].append(s)
        return list(obj.values())      
        # for val in obj.values():
        #         res.append(val)
        # return res