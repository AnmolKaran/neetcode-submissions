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
        mapping = {}
        while curr:
            nextNode = curr.next
            mapping[curr] = Node(curr.val,curr.next,curr.random)
            curr = nextNode
        
        prev = None
        curr = head
        
        while curr:
            nextNode = curr.next
            cpy = mapping[curr]
            if curr.next:
                cpy.next = mapping[curr.next]
            else:
                cpy.next = None
            if curr.random:
                cpy.random = mapping[curr.random]
            else:
                cpy.random = None
            prev = curr
            curr = nextNode
        return mapping[head] if head else None
        

