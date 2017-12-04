# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:

    def countofList(self, A):
        current = A
        i= 0
        if A is None:
            return i
        while current is not None:
            i += 1
            current = current.next
        return i;

    def reverseList(self, A):
        prev = None
        current = A
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def removeNode(self, A, B):
        current = A
        prev = None
        i = 1
        #print('A:'+str(A.val))
        while i < B:
            prev = current
            current = current.next
            '''
            if prev is not None:
                print('prev:'+str(prev.val))
            print('current:'+str(current.val)+' at i='+str(i))
            '''
            i+=1

        #print('prev:'+str(prev))
        if prev is None:
            A = current.next
            return A
        #print('prevval:'+str(prev.val))

        if current is None:
            prev.next = None
            #print('current is None')
        else:
            #print('current val:'+str(current.val))
            #print('prev next:'+str(prev.next.val))
            #print('current next:'+str(current.next.val))
            prev.next = current.next

        return A



    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        a_count = self.countofList(A)
        if a_count ==0:
            return A

        if a_count<=B or a_count==1 :
            return A.next

        #B is less than n and n > 1
        R = self.reverseList(A)
        C = self.removeNode(R, B)
        A = self.reverseList(C)
        return A
