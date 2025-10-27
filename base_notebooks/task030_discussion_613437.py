def p(m):
    a=[0]*len(f:=sum(m,[]));I=f.index;l=I(1)%10
    for i,v in enumerate(f):
        if v&1:a[i]=1;a[I(2)%10+i-l]=2;a[I(4)%10+i-l]=4
    return[*zip(*10*[iter(a)])]