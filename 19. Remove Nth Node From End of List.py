# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        len = 0
        cur = head
        # print(cur.val)
        while cur is not None:
            len+=1
            cur = cur.next
        print("len is", len)
        
        
        target = len - n +1 
        
        print("tar is", target)
        i = 1
        cur = head
        
        if len == 1:
            cur.val = None
            return
        if target ==1:
            cur = cur.next
            print(cur,cur.val,cur.next)
            return cur
        
        # print("1 ok")
        while i<=target:
            print(i, target)
            print(cur)
            # print("loop ok")
            if i==target-1:
                
                print("in ok")
                cur.next = (cur.next).next
                break
            i+=1
            cur = cur.next
            
#         while i<=target:
            
#             # print("loop ok")
#             if i==target:
#                 if target==0:
#                     print("ok")
#                     cur.val = None
#                     return
#                 print(cur)
#                 # print("in ok")
#                 cur.next = (cur.next).next
#             i+=1
#             cur = cur.next
            
        # print(head)
        return head
            
        
            
        