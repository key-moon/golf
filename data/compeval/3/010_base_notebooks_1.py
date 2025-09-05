def p(g):
    H,W=len(g),len(g[0]) if g else 0
    vis=[[False]*W for _ in range(H)]
    comp=[[0]*W for _ in range(H)]
    color=1
    
    def dfs(i,j,val):
        if i<0 or i>=H or j<0 or j>=W or vis[i][j] or g[i][j]!=val: return
        vis[i][j]=True
        comp[i][j]=color
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            dfs(i+di,j+dj,val)
    
    for i in range(H):
        for j in range(W):
            if not vis[i][j] and g[i][j]!=0:
                dfs(i,j,g[i][j])
                color+=1
    
    return comp