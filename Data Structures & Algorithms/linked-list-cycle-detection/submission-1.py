# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        visited.add(curr)
        if not curr:
            return False
        while curr.next:
            
            if curr.next in visited:
                return True
            visited.add(curr.next)
            curr = curr.next

        return False