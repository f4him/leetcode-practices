class Solution(object):
    def combine(self, n, k):
        res = []
        
        def bt(start, com):
            if len(com) == k:
                res.append(com[:])
                return
            
            for i in range(start, n+1):
                com.append(i)
                bt(i+1, com)
                com.pop()
        bt(1,[])
        
        return res
        