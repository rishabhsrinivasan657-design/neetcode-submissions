# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head.next

        #To reach midpt
        while fast and  fast.next:
            slow=slow.next
            fast=fast.next.next
        
        temp1=slow.next
        temp2=None
        temp3=slow.next
        slow.next=None

        #reverse the second list
        while temp1:
            temp3=temp1.next
            temp1.next=temp2
            temp2=temp1
            temp1=temp3

        
        
        start=head
        maxSum=0

        while temp2:
            maxSum=max(maxSum, start.val + temp2.val)
            start=start.next
            temp2=temp2.next
        
        return maxSum



        