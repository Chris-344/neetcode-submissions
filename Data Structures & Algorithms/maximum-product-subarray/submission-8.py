class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd=maxProd=res=nums[0]

        for n in nums[1:]:
            curMin,curMax=minProd,maxProd
            minProd=min(n,n*curMax,n*curMin)
            maxProd=max(n,n*curMax,n*curMin)
            res=max(maxProd,res)
        
        return res