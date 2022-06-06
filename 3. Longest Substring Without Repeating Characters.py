class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        alpha = set()
        i=0
        j=0
        max = 0
        while ( i < len(s)):
            
            if s[i] in alpha:
                alpha.remove(s[j])
                j+=1
            else:
                
                cur = i - j +1
                if max<cur:
                    max = cur
                # print(max)
                alpha.add(s[i])
                i+=1
        return max
                
        
                    
                