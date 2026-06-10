# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        og = pointer = prev
        prev = None
        for i in range(n-1):
            
            prev = pointer
            # if not pointer.next:
            #     return head
            pointer = pointer.next
        
        if prev  == None:
            og = pointer.next
        else:  
            prev.next = pointer.next
            pointer.next = None
        
        
        prev = None
        curr = og
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
                    