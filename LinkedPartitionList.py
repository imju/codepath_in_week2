# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        part_start = None
        part_prev = None
        current = A
        while current is not None and part_start is None:
            if current.val >= B:
                part_start = current
                break
            part_prev = current
            current = current.next


        if part_start is None:
            return A
        part = part_start.next
        prev = part_start
        less_list = []
        while part is not None:
            if part.val < B:
                prev.next = part.next
                if part_prev is None:
                    A = part
                else:
                    part_prev.next = part
                part_prev = part
                part.next = part_start
                part = prev.next
            else:
                #moving
                prev = part
                part = part.next
        return A
