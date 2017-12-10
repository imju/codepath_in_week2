# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def insertNodeEnd(self, current, val):
        node = ListNode(val)
        if current is None:
            return node
        else:
            current.next = node
        return node
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A is None:
            return A
        if A.next is None:
            return A

        dup_head = None
        dup_current = None
        prev = A
        current = A.next
        dup_found = False
        i=2
        while current is not None:
            #print 'i:'+str(i)+':prev.val:'+str(prev.val)+':current.val:'+str(current.val)+":dup_found:"+str(dup_found)
            if prev.val == current.val:
                if not dup_found :
                    if dup_head is None:
                        dup_head =  dup_current = self.insertNodeEnd(dup_head, i-1)
                    else:
                        dup_current = self.insertNodeEnd(dup_current,i-1)
                    #print'dup_start:'+str(dup_current.val)+' at '+str(i-1)
                    dup_found = True
            else:
                if dup_found:
                    dup_found = False
                    dup_current = self.insertNodeEnd(dup_current, i-1)
                    #print'dup_end:'+str(dup_current.val)+' at ' +str(i-1)

            i+=1
            prev = current
            current = current.next
        if dup_found:
            self.insertNodeEnd(dup_current, i-1)

        dup_current = dup_head
        '''
        while dup_current is not None:
            print 'dup_current:'+str(dup_current.val)
            dup_current = dup_current.next
        '''

        dup_current = dup_head
        current = A
        i = 1
        prev_dup_end = 0
        move_head = False
        while dup_current is not None:
            dup_start = dup_current.val
            dup_current = dup_current.next

            dup_end = dup_current.val
            '''
            print 'prev_dup_end:'+str(prev_dup_end)
            print 'dup_start:'+str(dup_start)
            print 'dup_end:'+str(dup_end)
            '''
            if dup_start == 1 :
                move_head = True
                dup_pre_node = A
            end_done = False
            while current is not None and not end_done:

                if i == dup_start-1:
                    if move_head:
                        if dup_start - prev_dup_end > 1 :
                           move_head = False
                    dup_pre_node = current


                if i == dup_end :
                    #print'dup_end:'+str(dup_end)+' :dup_pre_node:'+str(dup_pre_node.val)+' :move_head:'+str(move_head)
                    if move_head :
                        A = current.next
                    else:
                        dup_pre_node.next = current.next
                    end_done = True

                current = current.next
                i += 1


            #print 'A:'+str(A.val)

            dup_current = dup_current.next
            prev_dup_end = dup_end

        return A
