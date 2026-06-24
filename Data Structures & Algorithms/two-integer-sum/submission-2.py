class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj={}
        for i,j in enumerate(nums):
                diff=target-j
                if diff in obj:
                        return [obj[diff],i]
                obj[j]=i
# 1 2 4 6
# 7