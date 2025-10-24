def p(I,t=range):
 def c(m):p={};[p.__setitem__(j,p.get(j,0)+1)for a in m for j in a];return max(p,key=p.get)
 u=c(I);H,J=len(I),len(I[0]);e=[[0]*J for p in t(H)];P=[]
 for p in t(H):
  for j in t(J):
   if e[p][j]or I[p][j]==u:continue
   z=[(p,j)];e[p][j]=1;j=[]
   while z:D,E=z.pop();d=I[D][E];j.append((d,(D,E)));[z.append((p,j))or e[p].__setitem__(j,1)for(p,j)in[(D-1,E),(D+1,E),(D,E-1),(D,E+1)]if 0<=p<H and 0<=j<J and not e[p][j]and I[p][j]!=u]
   P.append(j)
 K=lambda s:list(s)if not s or not(isinstance(next(iter(s)),tuple)and len(next(iter(s)))==2and isinstance(next(iter(s))[1],tuple))else[p for(j,p)in s]
 def F(s):p=K(s);j,a=[p for(p,j)in p],[p for(j,p)in p];return min(j),max(j),min(a),max(a)
 R=lambda s:0if not s else F(s)[1]-F(s)[0]+1;S=lambda s:0if not s else F(s)[3]-F(s)[2]+1;T=lambda s:F(s)[0];o=lambda s:F(s)[1];p=lambda s:F(s)[2];b=lambda s:F(s)[3];z=lambda s:S(K(s))==1and R(K(s))==len(K(s))if K(s)else 0
 def c(a,b):p,j,a,D=*a,*b;E,F,G,H=min(p,a),max(p,a)+1,min(j,D),max(j,D)+1;return{(p,j)for j in t(G,H)}if p==a else{(p,j)for p in t(E,F)}if j==D else{(p,j)for(p,j)in zip(t(E,F),t(G,H))}if a-p==D-j else{(p,j)for(p,j)in zip(t(E,F),t(H-1,G-1,-1))}if a-p==j-D else set()
 d=lambda z,g:c(z,(z[0]+42*g[0],z[1]+42*g[1]));q=[]
 for G in P:
  a={j for(p,j)in G if p==2}
  if not a:continue
  N,s,j,k=o(a)==o(G),b(a)==b(G),T(a)==T(G),p(a)==p(G);r,i=(1if N else 0)+(-1if j else 0),(1if s else 0)+(-1if k else 0);D,E=T(a)+R(a)//2,p(a)+S(a)//2;e=d((D,E),(r,i));q.append(e)
 o={j for p in q for j in p};N=[list(p)for p in I]
 for(p,j)in o:
  if 0<=p<H and 0<=j<J:N[p][j]=2
 o=set()
 for(G,e)in zip(P,q):
  s=z(e);a=min(R(G),S(G))
  for b in t(-(a-1),a):
   if s:o.update({(p,j+b)for(p,j)in e})
   else:o.update({(p+b,j)for(p,j)in e})
 for(p,j)in o:
  if 0<=p<H and 0<=j<J and N[p][j]==u:N[p][j]=3
 return N