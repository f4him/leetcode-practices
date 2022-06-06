class Solution(object):
    def orangesRotting(self, grid):
        ROW, COL  = len(grid), len(grid[0])
        fresh, time = 0,0
        q = []
        
        for i in range(ROW):
            for j in range(COL):
                
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append([i,j])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        
        
        while q and fresh > 0:
            time+=1
            for i in range(len(q)):
                print(q)
                r,c = q.pop(0)
                print(q, "after popping", r,c)
                for m,n in direction:
                    nr, nc = r+m, c+n
                    if nr<0 or nr==ROW or nc<0 or nc==COL or grid[nr][nc] == 2 or grid[nr][nc]==0:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 2
                    fresh-=1
                    print(q,grid, time, fresh)
            
            
        return time if fresh == 0 else -1
                        
            
        
        
        