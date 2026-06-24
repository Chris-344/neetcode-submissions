class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj={}
        freq=[[]for i in range (len(nums) + 1)]
        for i in nums:
            obj[i]=1+obj.get(i,0)
        for n,c in obj.items():
            freq[c].append(n)
        
        res=[]
        for arr in range(len(freq)-1,0,-1):
            for i in freq[arr]:
                 res.append(i)
                 if len(res)==k:
                    return res