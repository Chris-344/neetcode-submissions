# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(node,node2,carry):
            if not node and not node2:
                return ListNode(carry) if carry else None
            if not node:
                total=node2.val+carry
                curr=ListNode(total%10)
                curr.next=recurse(None,node2.next,total//10)
                return curr
            if not node2:
                total=node.val+carry
                curr=ListNode(total%10)
                curr.next=recurse(node.next,None,total//10)
                return curr
            total=node.val+node2.val+carry
            res=ListNode(total%10)
            res.next=recurse(node.next,node2.next,total//10)
            return res
        res=recurse(l1,l2,0)
        return res