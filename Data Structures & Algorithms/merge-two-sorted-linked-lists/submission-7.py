# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
 
        temp=ListNode()
        
        if curr1 and not curr2:
            temp.val=curr1.val
            curr1=curr1.next
        elif curr2 and not curr1:
            temp.val=curr2.val
            curr2=curr2.next

        elif curr1 and curr2:
            if curr1.val < curr2.val:
                temp.val=curr1.val
                curr1=curr1.next
            else:
                temp.val=curr2.val
                curr2=curr2.next
        elif not curr1 and not curr2:
            return None       
        
        res=temp


        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp.next=ListNode(curr1.val)
                curr1=curr1.next
            else:
                temp.next=ListNode(curr2.val)
                curr2=curr2.next
        
            temp=temp.next
                
        while curr1:
                temp.next=ListNode(curr1.val)
                curr1=curr1.next
                temp=temp.next
        while curr2:
                temp.next=ListNode(curr2.val)
                curr2=curr2.next
                temp=temp.next


        
        return res
        """
        compare 1 and 2

        """