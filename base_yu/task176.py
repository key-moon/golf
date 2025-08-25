# best: 76(joking+MWI, joking/MWI, joking) / others: 77(luke), 77(luke/sisyphus/Seek), 78(mukundan), 80(dbdr), 86(kabutack)
# =================================== 76 ===================================
# p=lambda g:[[v or(abs(j%12-6)+i<2 or abs((j+6)%12-6)<i)*4 for j,v in enumerate(g[i])]for i in range(3)]

# p=lambda g:[(s*9)[:len(g[0])]for s in[[2,0,0,0,2,4,4,4,2,0,0,0],[4,2,0,2,0,2],[4,4,2,0,0,0,2,0,0,0,2,4]]]


# a=[[2,4,4],[0,2,4],[0,0,2],[0,2,0],[2,0,0],[4,2,0],[4,4,2]]
# a+=a[5:0:-1]
# p=lambda g:[*zip(*(a*9)[:len(g[0])])]

a=[2,0,0,0,2,4,4,4,2,0,0,0]*2
p=lambda g:[(s*9)[:len(g[0])]for s in[a,[4,2,0,2,0,2],a[6:18]]]


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