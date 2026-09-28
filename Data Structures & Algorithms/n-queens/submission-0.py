class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["." ]*n for _ in range(n)]
        res=[]
        def backtrack(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if self.isSafe(board,r,c):
                    board[r][c]="Q"
                    backtrack(r+1)
                    board[r][c]="."

            

        backtrack(0)
        return res
   

    def isSafe(self,board,r,c):        
        row=r-1
        while row>=0:
            if board[row][c]=="Q":
               return False
            row=row-1
        

        row,col=r-1,c+1
        while row>=0 and col<len(board):
            if board[row][col]=="Q":
                return False
            row,col=row-1,col+1


        row,col=r-1,c-1
        while row>=0 and col>=0:
            if board[row][col]=="Q":
                return False
            row,col=row-1,col-1

        return True






        





