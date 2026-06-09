# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        # put the list into a stack
        listStack = []
        curNode = head;
        curPrev = None
        while (curNode):
            if (curPrev == None):
                curPrev = curNode
                curNode = curNode.next
                curPrev.next = None
            else:
                thisNode = curNode
                curNode = curNode.next
                thisNode.next = curPrev
                curPrev = thisNode
        
        return curPrev