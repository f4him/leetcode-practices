
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        m = set()
        
        temp =headA
        while temp:
            m.add(temp.val)
            temp = temp.next
            
        temp = headB
        while temp:
            if temp.val in m:
                return temp.val
            temp=temp.next    
        
        
        