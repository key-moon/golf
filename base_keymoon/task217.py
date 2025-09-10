# best: 95(jailctf merger, xsot ovs att joking mewheni) / others: 96(4atj sisyphus luke Seek mukundan), 106(natte), 107(kabutack), 109(2F), 109(biz)
# 155
# M=max
# r=range(3)
# b=[(i,j) for i in r for j in r]
# def p(g):
#  m=M(g).index(M(M(g)))
#  p=[*filter(M,g)]
#  return[[p[I][m+J]*bool(p[i][m+j]) for j,J in b]for i,I in b]
# 130
# M=max
# r=range(9)
# def p(g):
#  m=M(g).index(M(M(g)))
#  p=[*filter(M,g)]*3
#  return[[p[i][m+j%3]*bool(p[i//3][m+j//3]) for j in r]for i in r]
# 143
# E=lambda g:[*filter(max,zip(*g))]*3
# F=lambda r,R:zip(r,(R+R[1:]*2)[::3])
# def p(g):
#  p=E(E(g))
#  return[[c*(0<d) for c,d in F(r,R)]for r,R in F(p,p)]
# 121
# r=range(9)
# def p(g):
#  p=[*filter(max,zip(*filter(max,zip(*g))))]
#  return[[p[i%3][j%3]*(0<p[i//3][j//3]) for j in r]for i in r]
# 121
r=range(9)
E=lambda g:[*filter(max,zip(*g))]*3
def p(g):
 p=E(E(g))
 return[[p[i][j]*(0<p[i//3][j//3]) for j in r]for i in r]










