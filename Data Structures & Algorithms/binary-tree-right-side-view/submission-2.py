# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        que=collections.deque()
        que.append(root)
        if not root:
            return []
        while que:
            n=len(que)
            for i in range(n):
                cur=que.popleft()
                if i==n-1:
                    res.append(cur.val)
                if cur.left:que.append(cur.left)
                if cur.right:que.append(cur.right)
        return res