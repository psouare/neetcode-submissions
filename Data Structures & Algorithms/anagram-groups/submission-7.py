class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rt=[]
        used=dict()
        for i in range(len(strs)) :
            used[i]=False
        for i in range(len(strs)) :
            if used[i]:
                continue
            group=[strs[i]]
            used[i]=True
            for j in range(i+1,len(strs)):
                if(Counter(strs[j])==Counter(strs[i])) and not used[j]:
                    group.append(strs[j])
                    used[j]=True
            rt.append(group)
        return rt