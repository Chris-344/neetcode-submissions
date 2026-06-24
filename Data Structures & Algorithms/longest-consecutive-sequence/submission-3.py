class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet=set(nums)
        longest=0
        for i in nums:
                length=0
                if i-1 not in mySet:
                        while (i+length) in mySet:
                                length+=1
                longest=max(longest,length)
        return longest