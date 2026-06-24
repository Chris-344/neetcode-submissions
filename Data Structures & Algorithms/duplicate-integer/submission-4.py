class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        obj={}
        for i in nums:
                if i in obj:
                        return True
                else:
                        obj[i]=1
        return False