class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c=Counter(s1)
        l=0
        k=len(s1)
        while(l<=len(s2)-k):
            if(Counter(s2[l:l+k])==s1c):
                return True
            l+=1
        
        return False

        