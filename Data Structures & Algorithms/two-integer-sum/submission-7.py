class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj={}
        for i,j in enumerate(nums):
            dif=target-j
            if dif in obj:
                return [obj[dif],i]
            obj[j]=i
        