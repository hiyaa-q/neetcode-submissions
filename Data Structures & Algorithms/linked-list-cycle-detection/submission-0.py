# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mySet = set()
        curNode = head
        while (curNode):
            if curNode in mySet:
                return True
            else:
                mySet.add(curNode)
                curNode = curNode.next
        
        return False
        