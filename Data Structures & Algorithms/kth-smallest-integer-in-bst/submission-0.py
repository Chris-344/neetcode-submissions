# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk=[]
        def inorder(node):
            if not node:return
            inorder(node.left)
            stk.append(node.val)
            inorder(node.right)

        inorder(root)
        return stk[k-1]
        
        

            



    """
    do inorder traversal till the length of the stack is k-1
    """