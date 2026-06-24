class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj={}
        for i,j in enumerate(nums):
                if target-j in obj:
                        return [obj[target-j],i]
                else:
                        obj[j]=i