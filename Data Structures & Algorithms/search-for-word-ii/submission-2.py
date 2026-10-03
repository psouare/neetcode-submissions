class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
            
    def addWord(self,word):
        cur =self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
                
        cur.word=True
            
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS,COLS=len(board),len(board[0])
        root=TrieNode()
        visit=set()
        res=set()
        for word in words:
            root.addWord(word)
        

        def dfs(r,c,node,w):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r,c) in visit or board[r][c] not in node.children):
                return
            

            visit.add((r,c))
            node=node.children[board[r][c]]
            w+=board[r][c]
            if node.word:
                res.add(w)

            dfs(r-1,c,node,w)
            dfs(r+1,c,node,w)
            dfs(r,c-1,node,w)
            dfs(r,c+1,node,w)

            visit.remove((r,c))
     

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        
       
        return list(res)
        

        

       

        


        