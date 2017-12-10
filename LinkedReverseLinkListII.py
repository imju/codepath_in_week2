# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def reverse(self, p, i, m, n):
        if i == n:
            return (p.next, p)
        (end, top) = self.reverse(p.next, i+1, m, n, prev)
        q = p.next
        q.next = p
        p.next = end
        return (end, top)

    def reverseIter(self, p, i, n):

        prev = None
        current = p
        while current is not None and i <= n:
            following = current.next
            current.next = prev
            prev = current
            current = following
            i+=1
        return (prev, current)




    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if A.next is None:
            return A
        current = A
        prev = None
        i = 1
        while i < B:
            prev = current
            current = current.next
            i+=1
        #(end, top) = self.reverse(current, B, B, C)
        (end, top) = self.reverseIter(current, i, C)
        current.next = top

        if prev is None:
            A = end
        else:
            prev.next = end

        return A
