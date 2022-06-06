class Solution(object):
    def updateMatrix(self, mat):
        row,col = len(mat),len(mat[0])
        q = []
        
        for r in range(row):
            for c in range(col):
                
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = "#"
                    
        for r,c in q:
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                nr = r+dx
                nc = c+dy
                # print("mat[r][c]")
                if nr>=0 and nr<row and nc>= 0 and nc<col and  mat[nr][nc] == "#":
                    print("mat[r][c]")
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        return mat