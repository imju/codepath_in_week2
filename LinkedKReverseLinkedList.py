# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:

    def reverseSubList(self, L, n):
        prev = None
        new_end = current = L

        i = 0
        while i < n and current is not None:
            print("at i="+str(i)+": :"+str(current.val))
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            i+=1
        new_start = prev
        return (new_start, new_end)

    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B==1:
            return A
        if A is None:
            return A
        prev_start = None
        start = A
        prev_end = None
        end = A
        new_head = None
        i=0
        while end is not None:
            if i < B: #move end
                print('end:'+str(end.val)+' at i='+str(i))
                prev_end = end
                end = end.next
                i += 1
            else:
                print('start:'+str(start.val))
                (new_start, new_end) = self.reverseSubList(start,B)
                print('new_start:'+str(new_start.val))
                print('new_end:'+str(new_end.val))
                print('new_end:next'+str(new_end.next))
                if prev_start is None:
                    new_head = new_start
                    prev_end = new_end
                else:
                    prev_start = new_start
                    prev_end = new_end
                print('new_head:'+str(new_head.val))
                prev_start = new_end
                start = end.next
                end = end.next
                i=0

        return  new_head
