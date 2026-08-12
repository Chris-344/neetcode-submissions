class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = maxProd = res = nums[0]

        for num in nums[1:]:
            curMin, curMax = minProd, maxProd

            minProd = min(num, curMin * num, curMax * num)
            maxProd = max(num, curMin * num, curMax * num)

            res = max(res, maxProd)

        return res