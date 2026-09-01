# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast,c =head,0

        while fast:
            fast=fast.next
            c+=1
        
    
        ig=c-n
        if ig==0:
            return head.next
        ptr,i=head,0

        while i<ig-1:
            ptr=ptr.next
            i+=1

        tmp=ptr.next.next
        ptr.next=tmp
        

        return head