def p(a):
    h,w=len(a),len(a[0])
    while 1:
        f=0
        for y in range(h):
            for x in range(w):
                if a[y][x]==0:
                    # four possible inward‐corner orientations
                    if y and x and a[y-1][x]==1 and a[y][x-1]==1 and a[y-1][x-1]==1: a[y][x]=2;f=1
                    elif y and x<w-1 and a[y-1][x]==1 and a[y][x+1]==1 and a[y-1][x+1]==1: a[y][x]=2;f=1
                    elif y<h-1 and x and a[y+1][x]==1 and a[y][x-1]==1 and a[y+1][x-1]==1: a[y][x]=2;f=1
                    elif y<h-1 and x<w-1 and a[y+1][x]==1 and a[y][x+1]==1 and a[y+1][x+1]==1: a[y][x]=2;f=1
        if not f: break
    return a
