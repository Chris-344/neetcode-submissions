class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj={}
        for i,k in enumerate(nums):
            if target-k in obj:
                return [obj[target-k],i]
            obj[k]=i
        