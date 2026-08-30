class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj=Counter(nums)
        freq=defaultdict(list)

        for key,val in obj.items():
            freq[val].append(key)

        res=[]
        for i in range(len(nums),-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
