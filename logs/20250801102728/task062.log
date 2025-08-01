import sys
def p(g):
    n=len(g);r=[(i,j,g[i][j])for i in range(n)for j in range(n)if g[i][j]>1]
    if not r: return [[3]*n for _ in g]
    C=max(v for *_,v in r)
    H=[i for i,j,v in r if v==C];hs,he=min(H),max(H)
    V=[j for i,j,v in r if v==C];vs,ve=min(V),max(V)
    mrow=(hs+he)//2;mcol=(vs+ve)//2
    out=[[3]*n for _ in g]
    for j in range(vs,ve+1): out[mrow][j]=C
    for i in range(hs,he+1): out[i][mcol]=C
    return out
# If run standalone, read a 10×10 grid of ints and print result
if __name__=='__main__':
    g=[list(map(int,line.split()))for line in sys.stdin]
    for row in p(g): print(*row)