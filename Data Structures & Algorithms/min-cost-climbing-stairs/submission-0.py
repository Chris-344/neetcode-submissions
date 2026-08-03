class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minArr=[0]*(len(cost)+1)

        for i in range(len(cost)-1,-1,-1):
            if i==len(cost)-1:
                minArr[i]=cost[-1]
                continue
            minArr[i]=cost[i]+min(minArr[i+1],minArr[i+2])
        return min(minArr[0:2])