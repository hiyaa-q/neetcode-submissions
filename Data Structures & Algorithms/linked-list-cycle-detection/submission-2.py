# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoisePtr = head
        harePtr = head
        while (tortoisePtr and harePtr):
            tortoisePtr = tortoisePtr.next
            harePtr = harePtr.next
            if (harePtr): harePtr = harePtr.next
            if tortoisePtr and tortoisePtr == harePtr:
                return True
        
        return False
        