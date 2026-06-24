class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj={}
        for i,j in enumerate(nums):
            diff=target-j
            if diff in obj:
                return [obj[diff],i]
            else:
                obj[j]=i