class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj={}
        for i in nums:
            obj[i]=1+obj.get(i,0)
        res=[]
        count = [[] for _ in range(len(nums)+1)]
        for fr,ky in obj.items():
            count[ky].append(fr)

        for i in range(len(count)-1,-1,-1):
            while count[i]:
                res.append(count[i].pop())
                if len(res)==k:
                    return res
            

"""
store the frequency of all the elements
go from  len of nums to 0
if array size equals k return the array

[3:5,5:6,2:1]
"""