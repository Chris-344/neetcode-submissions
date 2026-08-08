# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res=0
        def dfs(node:TreeNode,maxValue:int):
            if node.val>=maxValue:
                self.res+=1
            maxValue=max(maxValue,node.val)
            if node.left:dfs(node.left,maxValue)
            if node.right:dfs(node.right,maxValue)
        if not root:
            return 0
        dfs(root,root.val)

        return self.res
"""
maxValue
node.
"""