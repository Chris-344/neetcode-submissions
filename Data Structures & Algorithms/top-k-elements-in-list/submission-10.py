class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq={}

        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
            
    # you now have an obj with all your freqs
    # u would need to have an obj where the key is the freq and the value 
    # is an array where all the elements of that freq is stored
        count=[[] for _ in range(len(nums)+1)]
        
        for val,fr in freq.items():
            count[fr].append(val)
        
        for ele in range(len(count)-1,-1,-1):
            for x in count[ele]:
                res.append(x)
                if len(res)==k:
                    return res