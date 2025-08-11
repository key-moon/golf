def p(a):
    t=(0,0,0,0)
    h,w=len(a),len(a[0])
    for x in range(w):
        for y in range(x+1,w):
            for r in range(h):
                if a[r][x]==a[r][y]!=0:
                    s=1
                    while r+s<h and a[r+s][x]==a[r+s][y]!=0: s+=1
                    if s>t[0]: t=(s,r,x,y)
    return [row[t[2]:t[3]+1] for row in a[t[1]:t[1]+t[0]]]
