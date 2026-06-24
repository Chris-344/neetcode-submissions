class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for _ in range(len(nums) + 1)]
        obj={}
        for i in nums:
                obj[i]=1 + obj.get(i,0)
        for key,val in obj.items():
                freq[val].append(key)
        
        res=list()
        for i in range(len(nums),0,-1):
                for j in freq[i]:
                        res.append(j)
                        if len(res)==k:
                                return res