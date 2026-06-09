# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        last = None

        while fast.next and fast.next.next:
            slow = slow.next
            last = fast
            fast = fast.next.next


        curr = slow.next
        slow.next = None
        prev = None
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        #print(prev.val,prev.next.val)

        pointer = head
        fin = og = ListNode()
        while prev and pointer:
            fin.next = pointer
            pointer = pointer.next
            fin = fin.next
            fin.next = prev
            prev = prev.next
            fin = fin.next

        if prev == None:
            fin.next = pointer
        else:
            fin.next = prev

        #return og.next

        

        

        
        

        