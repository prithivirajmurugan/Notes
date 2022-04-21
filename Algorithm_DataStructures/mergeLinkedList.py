class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = None


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if None in (l1, l2):
        return l1 or l2
    if l1.val <= l2.val:
        h1, h2 = l1, l2
    else:
        h1, h2 = l2, l1

    initial_node = h1

    while h1 and h2:
        temp = None
        while h1 and h1.val <= h2.val:
            temp = h1
            h1 = h1.next
        temp.next = h2
        h1, h2 = h2, h1
    return initial_node


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = Solution.mergeTwoLists(self, l1.next, l2)
            return l1
        else:
            l2.next = Solution.mergeTwoLists(self, l1, l2.next)
            return l2
