class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        obj=set()
        for i in nums:
                if i in obj:
                        return True
                else:
                        obj.add(i)
        return False