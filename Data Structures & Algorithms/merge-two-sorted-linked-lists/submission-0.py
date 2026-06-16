# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        newTail = None

        # edge case: one list is empty
        if (list1 == None): return list2
        elif (list2 == None): return list1

        # loop to add lists while they are both still full
        while (list1 != None and list2 != None):
            # init new node
            newNode = None
            if (list1.val < list2.val):
                newNode = list1
                list1 = list1.next
            else:
                newNode = list2
                list2 = list2.next

            # add next node to list
            if (not newHead):
                newHead = newNode
                newTail = newNode
                newNode.next = None
            else:
                newTail.next = newNode
                newTail = newNode
                newTail.next = None
        
        # add remaining list
        if (list1 == None):
            newTail.next = list2
        else:
            newTail.next = list1
        
        return newHead