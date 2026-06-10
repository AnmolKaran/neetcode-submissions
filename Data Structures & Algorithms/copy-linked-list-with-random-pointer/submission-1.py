"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        mapping = {None:None}
        while curr:
            nextNode = curr.next
            mapping[curr] = Node(curr.val,curr.next,curr.random)
            curr = nextNode
        
        prev = None
        curr = head
        
        while curr:
            nextNode = curr.next
            cpy = mapping[curr]
            
            cpy.next = mapping[curr.next]
            
     
            cpy.random = mapping[curr.random]
            
            prev = curr
            curr = nextNode
        return mapping[head] if head else None
        

