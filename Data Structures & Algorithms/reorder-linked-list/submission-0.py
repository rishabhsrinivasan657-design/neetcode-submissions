# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next

        #Finding Middle
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reversing second list
        second=slow.next
        prev=None
        temp=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        
        #Merge LinkedLists
        temp1=head
        temp2=prev
        slow.next=None
        start=head

        while prev:
            temp1=start.next
            temp2=prev.next
            start.next=prev
            prev.next=temp1
            prev=temp2
            start=temp1
        
        






        

        