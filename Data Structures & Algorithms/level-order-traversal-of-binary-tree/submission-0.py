# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        que=[]
        if root:que.append(root)

        while que:
            level=[]
            qlen=len(que)
            for i in range(qlen):
                temp=que.pop(0)
                if temp.left:que.append(temp.left)
                if temp.right:que.append(temp.right)
                level.append(temp.val)
            res.append(level)
        return res