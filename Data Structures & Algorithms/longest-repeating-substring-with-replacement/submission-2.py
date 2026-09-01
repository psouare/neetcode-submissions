class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxc=0
        count={}
        l=0
        re=0
        macx=0

        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            macx=max(count[s[r]],macx)


            while r-l+1 -macx>k:
                count[s[l]]-=1
                l+=1

            re=max(re,r-l+1)
        return re


