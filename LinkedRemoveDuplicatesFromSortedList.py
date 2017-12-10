# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 1 -> 1 -> 2
    # 1 -> 2 -> 2 -> 3
    # 1 -> 2 -> 2 -> 2 -> 3
    # 1 -> 2 -> 3 -> 3
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        # A has none
        if A is None:
            return A
        # A has only one
        if A.next is None:
            return A

        prev = None
        current = A
        while current is not None:
            next = current.next
            if prev is not None:
                if prev.val == current.val:
                    prev.next = next
                    current = next
                    continue
            prev = current
            current = next
        return A
