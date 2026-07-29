class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj={}
        for i,j in enumerate(nums):
            dif=target - j

            if dif not in obj:
                obj[j]=i
            elif dif in obj:
                return [obj[dif],i]