class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]


        def dfs(o,c,subset):

            if o==n and c==n:
                res.append("".join(subset))
                return
            

            if o<n:
                subset.append('(')
                dfs(o+1,c,subset)
                subset.pop()
            if c<o:
                subset.append(')')
                dfs(o,c+1,subset)
                subset.pop()
        
        dfs(0,0,[])
        return res



