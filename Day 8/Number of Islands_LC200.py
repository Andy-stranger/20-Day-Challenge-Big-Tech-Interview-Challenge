def numIslands(self, grid):

    def is_valid_coordinate(m,n):
        return m >= 0 and m < r and n >= 0 and n < c

    def bfs(k,l):
        q.append([k,l])
        while q:
            cur_r , cur_c = q.pop(0)
            if not is_valid_coordinate(cur_r,cur_c) or grid[cur_r][cur_c] == '0':
                continue
            grid[cur_r][cur_c] = '0'
            for i in range(4):
                new_r = cur_r + delta[i]
                new_c = cur_c + delta[i+1]
                if is_valid_coordinate(new_r,new_c) and grid[new_r][new_c] == '1':
                    q.append([new_r,new_c])

    r = len(grid)
    c = len(grid[0])
    vis = [[0]*c for _ in range(r)]
    ones = []
    delta = [-1,0,1,0,-1]
    count = 0
    q = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                count += 1
                bfs(i,j)                
    return count