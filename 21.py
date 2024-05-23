# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode() # this acts as a placeholder and initalize the ListNode() with dummy where val = 0 and next=None we have no link 
        # dummy = ListNode is similar to dummy = []
        tail = dummy # this initalize dummy node with val = 0 and next = head of the element both has same point start

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # appends node analogus
                list1 = list1.next # moves the pointer node analogus given this is a listnode
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next # when list1.val = list2.val? no
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next



solution = Solution()
print(solution.mergeTwoLists(list1, list2))