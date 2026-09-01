class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxS=0
        l,r=0,0
        charIndex={}
        
        for r in range(len(s)):
            if s[r] in charIndex and charIndex[s[r]]>=l:
                l=charIndex[s[r]]+1
            maxS=max(maxS,r-l+1)
            charIndex[s[r]]=r


        return maxS
                

            



        