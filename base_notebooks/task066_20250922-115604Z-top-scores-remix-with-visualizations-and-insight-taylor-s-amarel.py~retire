import copy
E=enumerate
A=range
S=sorted
N=None;G,R,B=3,2,0;d=copy.deepcopy
def ib(g,r,c):return 0<=r<len(g)and 0<=c<len(g[0])
def n(r,c):return[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
def ad(a,b):return a[0]+b[0],a[1]+b[1]
def sb(a,b):return a[0]-b[0],a[1]-b[1]
def nm(d):return tuple(map(lambda x:(x>0)-(x<0),d))
def rl(d):return-d[1],d[0]
def rr(d):return d[1],-d[0]
def m(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
def fp(g,v):return[(r,c)for r,rw in E(g)for c,x in E(rw)if x==v]
def c4c(ps):
 u,cs=set(ps),[]
 while u:
  s=u.pop();q=[s];c=[s]
  while q:
   r,i=q.pop()
   for nr,ni in n(r,i):
    if(nr,ni)in u:u.remove((nr,ni));q.append((nr,ni));c.append((nr,ni))
  cs.append(c)
 return cs
def cg(gs,p):return min(m(p,g)for g in gs)if gs else 1e9
def l(v):return v in(B,G)
def rs(g,s,f,rs):
 h,w=len(g),len(g[0]);o=d(g);v=set();k=0;p=s;md=cg(rs,p);ed=md;t=0
 while k<h*w*10:
  k+=1;np=ad(p,f)
  if ib(g,*np)and o[np[0]][np[1]]==R:break
  if not ib(g,*np)or not l(o[np[0]][np[1]]):
   t+=1;ld,rd=rl(f),rr(f);ts=[]
   for td in(ld,rd):
    tp=ad(p,td)
    if ib(g,*tp)and l(o[tp[0]][tp[1]]):ts.append((cg(rs,tp),td,tp))
   if ts:ts.sort(key=lambda x:(x[0],0 if x[1]==ld else 1));_,f,p=ts[0]
   else:
    rdi=-f[0],-f[1];rp=ad(p,rdi)
    if ib(g,*rp)and l(o[rp[0]][rp[1]]):f,p=rdi,rp
  else:p=np
  if o[p[0]][p[1]]==B:o[p[0]][p[1]]=G
  st=(p,f)
  v.add(st);dg=cg(rs,p);md=min(md,dg);ed=dg
 return o,k,md,ed,t
def ds(g):
 rp,gp=fp(g,R),fp(g,G)
 c=min(c4c(gp),key=lambda x:(len(x),cg(rp,(round(sum(r for r,_ in x)/len(x)),round(sum(c for _,c in x)/len(x))))))
 sc=set(c);sp=next((( (r,i),(nr,ni))for r,i in c for nr,ni in n(r,i)if(nr,ni)in sc),N)
 sp=sp or max(((p1,p2)for p1 in c for p2 in c),key=lambda x:m(*x))
 p1,p2=sp;f=nm(sb(p2,p1));rn=[rs(g,p2,f,rp),rs(g,p1,(-f[0],-f[1]),rp)]
 return S(rn,key=lambda x:(x[3],x[4],x[2],x[1]))[0][0]
def br(g):
 rp,gp=fp(g,R),fp(g,G)
 vp=lambda ps:S(ps)[0][1]==S(ps)[1][1]and abs(S(ps)[0][0]-S(ps)[1][0])==1
 (gr,gc),(gr2,_)=S(gp);(rr1,rc1),(rr2,_)=S(rp)
 if{gr,gr2}!={rr1,rr2}:return
 cs,ce=S([gc,rc1]);bw=N
 for r in A(min(gr,rr1)+1):
  if all(g[r][c]in(B,G,R)for c in A(cs,ce+1)):bw=r;break
 if bw in(N,0):return
 o=d(g);er=max(gr2,rr2)
 for r in A(bw,er+1):
  if o[r][gc]==B:o[r][gc]=G
  if o[r][rc1]==B:o[r][rc1]=G
 for c in A(cs,ce+1):
  if o[bw][c]==B:o[bw][c]=G
 return o
def p(g):return br(g)or ds(g)