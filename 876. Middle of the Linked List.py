# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        s, f = head, head
        
        if head.next == None:
            return head
        
        if (head.next).next == None:
            return head.next
            
        i=0
        while s.next:
            # print(i)
            # i+=1
            # if s.next:
            if f==None or f.next == None:
                return s
            f= (f.next).next
            
            s = s.next
        