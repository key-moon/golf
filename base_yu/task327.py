# best: 67(4atj sisyphus luke Seek mukundan, import itertools, jailctf merger, ox jam, biz) / others: 69(Tony Li), 72(jacekw Potatoman nauti natte), 72(cg-klogw-sekken), 72(JRKKX), 74(JRKX)
# =============================== 67 ==============================
# p=lambda g,R=range:[[max([g[i-k][j-k]for k in R(max(0,min(i,j)-2+abs(i-j)),min(i,j)+1)]+[0])for j in R(6)]for i in R(6)]
p=lambda g,R=range(6):[[max(3>i-k>-1<j-k<3and g[i-k][j-k]for k in R)for j in R]for i in R]

# def p(g):
#  u=[s+[0,0,0]for s in g]+[[0]*6 for _ in range(3)]
#  for i in range(1,6):
#   for j in range(1,6):
#    u[i][j]+=u[i-1][j-1]
#  return u
