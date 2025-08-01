def p(g):
    h,w=len(g),len(g[0])
    # find background color
    cnt={}
    for r in g:
        for x in r:
            cnt[x]=cnt.get(x,0)+1
    bg=max(cnt,key=cnt.get)
    # find connected components of non-bg
    v=[[0]*w for _ in range(h)]
    C=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]!=bg and not v[i][j]:
                c=g[i][j]
                stk=[(i,j)]
                v[i][j]=1
                pts=[]
                mi,mx,ni,nx=i,i,j,j
                while stk:
                    y,x=stk.pop()
                    pts.append((y,x))
                    if y<mi:mi=y
                    if y>mx:mx=y
                    if x<ni:ni=x
                    if x>nx:nx=x
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        Y,X=y+dy,x+dx
                        if 0<=Y<h and 0<=X<w and not v[Y][X] and g[Y][X]==c:
                            v[Y][X]=1
                            stk.append((Y,X))
                H=mx-mi+1;W=nx-ni+1
                s=H if H>W else W
                # extract shape and pad to s×s
                a=[[bg]*W for _ in range(H)]
                for y,x in pts:
                    a[y-mi][x-ni]=c
                dH=s-H;dW=s-W
                tH=dH//2;tW=dW//2
                b=[[bg]*s for _ in range(s)]
                for y in range(H):
                    for x in range(W):
                        if a[y][x]!=bg:
                            b[tH+y][tW+x]=a[y][x]
                C.append((s,b))
    # sort by size
    C.sort(key=lambda x:x[0])
    k=len(C)-1
    side=C[0][0]+2*k
    mid=side//2
    R=[[bg]*side for _ in range(side)]
    for i,(s,b) in enumerate(C):
        off=k-i
        st=mid-s//2-off
        for y in range(s):
            for x in range(s):
                if b[y][x]!=bg:
                    R[st+y][st+x]=b[y][x]
    return R
