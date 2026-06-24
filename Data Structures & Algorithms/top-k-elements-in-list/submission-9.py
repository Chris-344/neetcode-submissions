class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for _ in range(len(nums) + 1)]
        indFreq={}
        for i in nums:
                if i in indFreq:
                        indFreq[i]+=1
                else:
                        indFreq[i]=1
        
        for key,v in indFreq.items():
                freq[v].append(key)
        res=[]
        for arr in range(len(freq)-1,-1,-1):
                for x in freq[arr]:
                        res.append(x)
                        if len(res)==k:
                                return res
#[[][1][2][3]]