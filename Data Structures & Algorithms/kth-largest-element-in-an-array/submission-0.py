from _heapq import heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        while k>1:
            heappop(nums)
            k-=1
        return -nums[0]
"""
pop a max heap k times and return the largest element
"""