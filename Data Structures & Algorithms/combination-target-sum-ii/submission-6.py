class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return

            
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])

            cur.pop()
            j=i+1
            while j<len(candidates) and candidates[j]==candidates[i]:
                j+=1
            dfs(j,cur,total)
        dfs(0,[],0)
        return res