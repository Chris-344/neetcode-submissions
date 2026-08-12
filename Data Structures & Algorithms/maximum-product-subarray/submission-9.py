class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd=maxProd=res=nums[0]
        for n in nums[1:]:
            curMin,curMax=minProd,maxProd
            minProd=min(n,curMax*n,curMin*n)
            maxProd=max(n,curMax*n,curMin*n)
            res=max(res,maxProd)
        return res