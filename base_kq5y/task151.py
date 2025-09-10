# best: 108(xsot ovs att joking mewheni) / others: 112(4atj sisyphus luke Seek mukundan), 113(jailctf merger), 127(Bulmenisaurus), 129(dbdr), 129(jacekwl Potatoman nauti)
# ================================================== 108 ===================================================

#def p(j):A=lambda c:list(map(all,c)).index(1);E,k=A(j),A(zip(*j));j[E-1][k-1:k+2]=j[E+1][k-1:k+2]=[4]*3;j[E][k-1]=j[E][k+1]=4;return j

#f = lambda a: next(i for i,v in enumerate(a) if v)
#f = lambda a: a.index((set(a)-{0}).pop())
#f = lambda a: a.index(({*a}-{0}).pop())

#def p(g):
# f=lambda a:a.index(sum(a))
# x,y=f(g[0]),f(next(zip(*g)))
# for k in range(9):
#  if k-4:g[y+k//3-1][x+k%3-1]=4
# return g

def p(g):
 x=g[0].index(sum(g[0]));y=g.index(max(g))
 for k in range(9):
  if k-4:g[y+k//3-1][x+k%3-1]=4
 return g

#p=lambda g:exec('x=g[0].index(sum(g[0]));C,*_=zip(*g);y=C.index(sum(C))\nfor k in range(9):\n if k-4:g[y+k//3-1][x+k%3-1]=4')or g












