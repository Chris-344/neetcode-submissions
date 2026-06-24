class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val=set()
        for i in nums:
                if i in val:
                        return True
                val.add(i)
        return False