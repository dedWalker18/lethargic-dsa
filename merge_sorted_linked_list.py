## This is from leetcode Q 21

class LN:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dh = LN(None)
        t = dh

        while list1 and list2:
            if list1.val < list2.val:
                t.next = list1
                list1 = list1.next
            else:
                t.next = list2
                list2 = list2.next
            t = t.next

        t.next = list1 or list2

        return dh.next
    