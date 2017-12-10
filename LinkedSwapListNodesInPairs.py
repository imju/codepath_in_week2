# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        prev = None
        if A is None:
            return A
        if A.next is None:
            return A
        current = A

        while current is not None:
            following = current.next
            if following is None:
                break
            temp = following.next
            current.next = following.next
            following.next = current
            if prev is None:
                A = following
            else:
                prev.next = following
            prev = current
            current = temp

        return A
