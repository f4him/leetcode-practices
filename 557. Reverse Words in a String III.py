class Solution(object):
    def reverseWords(self, s):
        p = s.split()
        print(p)
        a = []
        for i in p:
            l=0
            r=len(i)-1
            new = [None]*len(i)
            while l<len(i):
                new[l]= i[r]
                l+=1
                r-=1
            a.append("".join(new))
        return(" ".join(a))