class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS =len(board),len(board[0])
        visit=set()

        def dif(r,c):
            if r<0 or c<0 or r==ROWS or c == COLS or (r,c) in visit or board[r][c]!="O":
                return
            board[r][c]="T"
            visit.add((r,c))
            dif(r+1,c)
            dif(r-1,c)
            dif(r,c+1)
            dif(r,c-1)

   
        for r in range(ROWS):
            if board[r][0]=="O":
                dif(r,0)           
            if board[r][COLS-1]=="O":
                dif(r,COLS-1)

        for c in range(COLS):
            if board[0][c]=="O":
                dif(0,c)
            if board[ROWS-1][c]=="O":
                dif(ROWS-1,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="T":
                    board[r][c]="O"


