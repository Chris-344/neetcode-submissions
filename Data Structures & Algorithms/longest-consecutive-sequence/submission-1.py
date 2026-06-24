class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet=set(nums)
        longest=0
        for i in nums:
                length=0
                if i-1 not in mySet:
                        length=0
                        while (length+i) in mySet:
                                length+=1
                longest=max(length,longest)
        return longest