class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS=len(grid),len(grid[0])
        q=deque()
        visit=set()
        fresh=0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1


        minu=0
        while fresh>0 and q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=2
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            
            minu+=1

        return minu if fresh==0 else -1







        
        