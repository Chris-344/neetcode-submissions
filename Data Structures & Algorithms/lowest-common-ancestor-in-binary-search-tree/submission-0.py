# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr=root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr=curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr=curr.right
            else:
                return curr
"""
if left is lesser and right is greater it is a subtree if we are traversing from above 
"""