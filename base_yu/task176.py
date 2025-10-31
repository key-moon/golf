# best: 61(ox jam) / others: 64(Code Golf International), 64(4atj sisyphus luke Seek mukundan), 64(jailctf merger), 67(HIMAGINE THE FUTURE.), 68(import itertools)
# ============================ 61 ===========================
# p=lambda g:[[v or(abs(j%12-6)+i<2 or abs((j+6)%12-6)<i)*4 for j,v in enumerate(g[i])]for i in range(3)]

# p=lambda g:[(s*9)[:len(g[0])]for s in[[2,0,0,0,2,4,4,4,2,0,0,0],[4,2,0,2,0,2],[4,4,2,0,0,0,2,0,0,0,2,4]]]


# a=[[2,4,4],[0,2,4],[0,0,2],[0,2,0],[2,0,0],[4,2,0],[4,4,2]]
# a+=a[5:0:-1]
# p=lambda g:[*zip(*(a*9)[:len(g[0])])]

# a=[2,0,0,0,2,4,4,4,2,0,0,0]*2
# p=lambda g:[(s*9)[:len(g[0])]for s in[a,[4,2,0,2,0,2],a[6:18]]]

# p=lambda g:[[v+(w>>i%12&1)*4for i,v in enumerate(s)]for s,w in zip(g,[224,65,2051])]
# p=lambda g:[(u:=0)or[((u:=(u+v)%3)==d)*(4-v*2)+v for v in s]for s,d in zip(g,[1,0,0])]
# p=lambda g,d=2:[(u:=d,d:=0)and[((u:=u+v)%3==d)*(4-v*2)+v for v in s]for s in g]
# p=lambda g,d=2:[(u:=d,d:=0)and[(v^-((u:=u+v)%3==d))%5for v in s]for s in g]
# p=lambda g,d=2:[([(v^-((d:=d+v)%3<1))%5for v in s],d:=0)[0]for s in g]
# p=lambda g,d=2:[[(v^-((d:=d+v)%3<1))%5for v in s]*-~(d:=0)for s in g]
p=lambda g,d=0:[[(v^-((d:=d+v)%3%2))%5for v in s]*(d:=1)for s in g]

# 2,5,...
# 0,3,...
# 0,3,...

# 1,0
# 2,0
# 2,1
# 0,5
# 0,6
# 1,6


# def p(g):
#  n=len(g[0])
#  g[1][::6]=[4]*((n-1)//6+1)
#  return g

#  1:1
#  5:1
#  6:2
