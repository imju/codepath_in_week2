# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def insertNode(self, prev, val):
        new_node = ListNode(val)

        if prev is not None:
            prev.next = new_node
        return new_node

    # A: None B: None
    # A: 2, 4, 3  B: 5, 6, 4
    # A: 8, 9, 2  B: 2, 8, 9, 5
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        current_a = A
        current_b = B
        result_h = None
        carry = 0
        while current_a is not None or current_b is not None:
            sum = carry
            if current_a is not None:
                sum += current_a.val
                current_a = current_a.next

            if current_b is not None:
                sum += current_b.val
                current_b = current_b.next

            carry = sum/10
            #print'sum%10:'+str(sum%10)
            if result_h is None:
                current = result_h = self.insertNode(result_h, sum%10)
            else:
                current = self.insertNode(current, sum%10)

        if carry > 0:
            current = self.insertNode(current, carry)

        return result_h
