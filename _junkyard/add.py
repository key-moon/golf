data = r"""
# task005.py
def p(m):
    _,Y,X,t=min([(sum(t:=[r[x:x+3]for r in m[y:y+3]],m).count(0),y,x,t)for y in range(19)for x in range(19)])
    for a in-4,0,4:
        for b in-4,0,4:
            for k in range(1,19):
                y=Y+a*k
                x=X+b*k
                for i in range(3):
                    for j in range(3):
                        if a|b!=0<=x+j<21>y+i>=0:m[y+i][x+j]=t[i][j]and max(max(r[X+b:X+b+3])for r in m[Y+a:Y+a+3])
    return m

# task018.py
def p(m):
    h=len(m)
    w=len(m[0])
    A,C,V=[],[],[]
    V=[]
    for q in [(z//w,z%w)for z in range(h*w)]:
        Y,X=[],[]
        q=[q]
        for y,x in q:
            if w>x>=0<=y<h and (y,x)not in V and m[y][x]:V+=(y,x),;Y+=y,;X+=x,;q+=(y-1,x),(y+1,x),(y,x-1),(y,x+1)
        if len(X)<4:A+=zip(Y,X)
        else:
            H=[r[min(X):max(X)+1]for r in m[min(Y):max(Y)+1]]
            H=[*zip(*H)]
            C+=H,
            H=H[::-1]
            C+=H,
            H=[*zip(*H)]
            C+=H,
            H=H[::-1]
            C+=H,
            H=[*zip(*H)]
            C+=H,
            H=H[::-1]
            C+=H,
            H=[*zip(*H)]
            C+=H,
            H=H[::-1]
            C+=H,
    G=[w*[0]for r in m]
    for y,x in [(z//w,z%w)for z in range(h*w)]:
        for c in C:
            if sum(I+y<h>0<w>J+x and m[I+y][J+x]==c[I][J] and (I+y,J+x)in A for I,J in [(z//len(c[0]),z%len(c[0]))for z in range(len(c[0])*len(c))])==3:
                for I,J in [(z//len(c[0]),z%len(c[0]))for z in range(len(c[0])*len(c))]:G[I+y][J+x]=c[I][J]
    return G


# task025.py
E=enumerate
def p(m):
    e={r[0]:y for y,r in E(m)if all(r)}
    if not e:return[*zip(*p([*map(list,zip(*m))]))]
    for y,r in E(m):
        for x,v in E(r):
            m[y][x]=0
            if v in e:m[(Y:=e[v])-(y<Y)+(y>Y)][x]=v
    return m

# task030.py
def p(m):
    a=[0]*len(f:=sum(m,[]));I=f.index;l=I(1)%10
    for i,v in enumerate(f):
        if v&1:a[i]=1;a[I(2)%10+i-l]=2;a[I(4)%10+i-l]=4
    return[*zip(*10*[iter(a)])]

# task076.py
def p(a):
    n=[]
    f=[divmod(sum(a,[]).index(1),len(a[0]))]
    for y,x in f:
        if 0<=x<len(a[0]) and 0<=y<len(a) and (y,x) not in n and a[y][x]:
            n+=(y,x),
            for i in-1,0,1:
                for j in-1,0,1:f+=(y+i,x+j),
    Y,X=zip(*n)
    o=[]
    H=[r[min(X):max(X)+1]for r in a[min(Y):max(Y)+1]]
    H=[*zip(*H)]
    o+=H,
    H=H[::-1]
    o+=H,
    H=[*zip(*H)]
    o+=H,
    H=H[::-1]
    o+=H,
    H=[*zip(*H)]
    o+=H,
    H=H[::-1]
    o+=H,
    H=[*zip(*H)]
    o+=H,
    H=H[::-1]
    o+=H,
    for y in range(len(a)):
        for x in range(len(a[0])):
            for c in o:
                if all(i+y<len(a) and j+x<len(a[0]) and (a[i+y][j+x]==c[i][j]or c[i][j]%2)for i in range(len(c))for j in range(len(c[0]))):
                    for i in range(len(c)):
                        for j in range(len(c[0])):a[i+y][j+x]=c[i][j]
    return a


# task090.py
import re
p=lambda g:exec(re.sub("@(.)",r"for \1 in range(",'b=()\n@in:=len(g)):m=len(g[0]);[b:=max(b,((I-i)*(J-j),i,j,I,J))@jm)@Ii+2,n+1)@Jj,m+1)if len({*f"{[g[Y][j:J]@Yi,I)]}0"})<6]\n@ib[1],b[3]):\n @jb[2],b[4]):g[i][j]=6'),{'g':g})or g

# task101.py
def p(a):
    V=[]
    q=[divmod(sum(a,[]).index(1),len(a[0]))]
    for y,x in q:
        if 0<=x<len(a[0]) and 0<=y<len(a) and a[y][x]and(y,x)not in V:V+=(y,x),;q+=(y-1,x),(y+1,x),(y,x-1),(y,x+1)
    Y,X=zip(*V)
    t=[r[min(X):max(X)+1]for r in a[min(Y):max(Y)+1]]
    for k in range(1,4):
        s=t
        s=[r for r in zip(*s)for _ in range(k)]
        s=[r for r in zip(*s)for _ in range(k)]
        for y in range(len(a)-len(s)+1):
            for x in range(-2,len(a[0])-len(s[0])+1):
                if all((y+i,x+j)not in V and(a[y+i][x+j]==2)==(s[i][j]==2)for j in range(len(s[0])) for i in range(len(s))):
                    for j in range(len(s[0])):
                        for i in range(len(s)):
                            if 0<=x+j:a[y+i][x+j]=s[i][j]
    return a


# task110.py
R=range(29)
p=lambda g:next([[max(r[x]for r in g[y%Y::Y])or g[y][x+9]for x in R]for y in R]for Y in R[4:]if all(len({*c,0})<3for i in R for c in zip(*g[i::Y])))

# task117.py
E=enumerate
def p(m):
    f=sum(m,[]);Y,X=divmod(f.index(*[c for c in{*f}if"2, 1, 2"in str([r.count(c)for r in m])!=f.count(c)<6]),len(m))
    for y,r in E(m):
        for x,v in E(r):
            if v:m[a:=2*Y+2-y][b:=2*X+2-x]=m[y][b]=m[a][x]=v
    return m

# task134.py
E=enumerate
def p(m,*Q):
    for c in(f:={*sum(m,[])}-{0}):Y,X=zip(*[(y,x)for y,r in E(m)for x,v in E(r)if v==c]);Q+=(max(Y)-min(Y)+1,c,min(Y),min(X)),
    n,c,y,x=min(Q);return[[(v==c)*sum(f,-c)for v in r[x:x+n:n//3]]for r in m[y:y+n:n//3]]

# task153.py
def p(g):R=range(10);e=[[0]*12];g=e+[[0,*r,0]for r in g]+e;return max([(sum(sum(m:=[[*map(max,g[i+y][j:j+3],g[I+y][J:])]for y in[0,1,2]],[]))*(max(i-I,j-J)>2),m)for i in R for j in R for I in R for J in R])[1]

# task165.py
def p(g):
    *g,=zip(*g)
    for v in sum(g,()):
        X=[x for x,c in enumerate(g)if v in c]
        if X[-1]-X[0]==6:
            for x in X:r=g[x];j=20-r[::-1].index(v);g[x]=r[:j]+(max(r[j:]),)*(20-j)
    return[*zip(*g)]

# task170.py
def p(g):f=sum(g,[]);k=max({*f}-{0},key=f.count);s=f"[i for i in zip(*%s)if i.count({k})>2]";n=len(c:=eval(s%s%"g"))//len(r:=[[*filter(int,r)][-4:]for r,s in zip(g,g[1:])if{*r,*s}-{k,0}][1:]);return[[r/k*c for r,c in zip(r,c[::n])]for r,c in zip(r,c[::n])]

# task260.py
R=range(10)
p=lambda m,k=7:-k*m or p([*zip(*[[(a:=max({*sum(m,())}-{5})if(y<1,0,0,5)==m[y][x:x+2]+m[y-1][x:x+2]else(x*y and m[y-1][x-1])|(x<9>y and m[y+1][x+1])|m[y][x])*(a!=5-9*k)for x in R]for y in R])],k-1)

# task264.py
p=lambda g,a=[9*[5]for _ in[0]*9],z=3:-z*a or[exec("if s[0][%s]!=5%s=s[1][1]:\n for r,R in zip(s,a):R[%s:%s]=r\n"*2%(*"1!360=03",))for i in range(len(g)-2)for j in range(len(g[0])-2)if{"0"}-{*str(s:=[r[j:j+3]for r in g[i:i+3]])}if a]and p(*[[*map(list,zip(*i[::-1]))]for i in(g,a)],z-1)

# task268.py
def p(p,n=range):
 i=len(p);a=lambda p:[*map(list,zip(*p[::-1]))]
 for k in n(4):
  h=[(t,z)for t in n(i)for z in n(i)if p[t][z]];z,h=zip(*h);z,g,f,e=min(z),max(z),min(h),max(h);t=p[z][f];d=p[z].count(t)
  if d<p[g].count(t):
   h,m=f+d//2,e-d//2
   for t in n(g):p[t][h:m+1]=[4]*(m-h+1)
   for t in n(z+1,g):p[t][f+1:e]=[4]*(e-f-1)
   for u in n(z+1):
    t=z-u
    if h>=u:p[t][h-u]=4
    if m+u<i:p[t][m+u]=4
   for t in n(4-k):p=a(p)
   return p
  p=a(p)

# task319.py
def p(g):
    b=max(sum(g,[]),key=sum(g,[]).count)
    a=[v for v in sum(g,[])if f"{b}, {v}, {b}"not in str(g+[*zip(*g)])][0]
    o=[[[b,a][v==a]for v in r[::2]]for r in g[::2]]
    m=[r*2for r in g*2]
    for i,r in enumerate(m):
        for j,v in enumerate(r):
            for k in{*sum(g,[])}:
                if[[[b,a][v==k]for v in r[j:j+len(o[0])]]for r in m[i:i+len(o)]]==o:
                    s=g
                    s=[[[b,k][v==k]for v in i]for i in zip(*s)if k in i]
                    s=[[[b,k][v==k]for v in i]for i in zip(*s)if k in i]
                    return s

# task324.py
def p(m):
    w=len(m[0])
    f=sum(m,[])
    d,e,b,c=sorted({*f},key=f.count)
    i=f.index(d)
    o=[f[Y+X]for Y,X in[(i,1),(i,-1),(i+w,0),(i-w,0)]if w>i%w+X>=0<=Y<w*len(m)].count
    for p,v in[*enumerate(f)]:
        for Y,X in(w,1),(w,-1),(-w,-1),(-w,1):
            i=p
            x=p%w
            while v in[d,e]and w>x>=0<=i<w*len(m):
                if f[i]==b:f[i]=[e,d][o(b)>o(c)]
                if f[i]==c:f[i]=[d,e][o(b)>o(c)]
                i+=Y+X
                x+=X
    return[*zip(*w*[iter(f)])]

# task355.py
E=enumerate
M=max
p=lambda g:[[M(a:=[m for i,r in E(g)for j,v in E(r)if(m:=M(a:=r[M(0,j-3):j+4]+[s[j]for s in g[M(0,i-3):i+4]if s!=r],key=a.count))!=v],key=a.count)]]

# task378.py
E=enumerate
p=lambda m:[[v or min(((Y:=abs(y-i))+(X:=abs(x-j)),3*v==sum(sum(s[j-1:j+2])for s in m[i-1:i+2])and(Y==X)*sum({*sum(m,[-v])}))for i,r in E(m)for j,v in E(r)if v)[1]for x,v in E(r)]for y,r in E(m)]

# task387.py
def p(m):
    (a,A),*_,(b,B)=P=[(y,x)for y,r in enumerate(m)for x,v in enumerate(r)if v]
    for t,(y,x)in enumerate(P):
        for u in-1,0,1:
            for v in-1,0,1:
                if u|v:m[y+u][x+v]=m[a][[B,A][0<t<3]]
    for i in range(2,(b-a)//4*2+1,2):m[a+i][A]=m[a+i][B]=m[b-i][A]=m[b-i][B]=5
    for i in range(2,(B-A)//4*2+1,2):m[a][A+i]=m[a][B-i]=m[b][A+i]=m[b][B-i]=5
    return m
"""

for code in data.split("# ")[1:]:
  name, actual = code.split("\n", 1)
  open(f"base_notebooks/{name.replace('.py', '_discussion_613437.py')}", "w").write(actual.strip())
