# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2= list2
        if curr1 == None:
            return curr2
        if curr2 == None:
            return curr1
        if  curr1.val <=curr2.val :
            main = curr1
            curr1 = curr1.next
        else:
            main = curr2
            curr2= curr2.next
        og = main
        while curr1 !=None and curr2 != None:
            if curr1.val <=curr2.val:
                main.next = curr1
                main = main.next
                curr1 = curr1.next
            else:
                main.next = curr2
                main = main.next
                curr2 = curr2.next

        if curr1:
            main.next = curr1
        else:
            main.next = curr2
        return og