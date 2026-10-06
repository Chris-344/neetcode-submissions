class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap=Counter(nums)
        arr=defaultdict(list)

        for ke,v in countMap.items():
            arr[v].append(ke)

        res=[]

        for i in range(len(nums),-1,-1):
            for n in arr[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return res