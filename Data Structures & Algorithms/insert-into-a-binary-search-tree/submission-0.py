# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        curr=root
        curr2=curr
        while curr:
            curr2=curr
            if curr.val > val:
                curr=curr.left
            elif curr.val < val:
                curr=curr.right
            else:
                break
        if val < curr2.val:
            curr2.left=TreeNode(val)
        elif val > curr2.val:
            curr2.right=TreeNode(val)
        return root