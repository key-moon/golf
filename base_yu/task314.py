# best: 96(natte) / others: 97(xsot ovs att joking mewheni), 101(4atj sisyphus luke Seek mukundan), 101(2F), 101(biz), 104(jailctf merger)
# ============================================= 96 =============================================
# p=lambda g,E=enumerate:[[max((min(j>2 and s[j-3],j<5 and s[j+3]),min(i>2 and t[i-3],i<5 and t[i+3]),s[j])) for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[max((min(s[j-3],j<5 and s[j+3]),min(t[i-3],i<5 and t[i+3]),s[j])) for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[max(min(s[j-3],(s*2)[j+3]),min(t[i-3],(t*2)[i+3]),s[j])for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[max(min((s*3)[j+5:j+12:6]),min((t*3)[i+5:i+12:6]),s[j])for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,R=range(8):[[max(min((g[i]*3)[j+5:j+12:6]),min(g[i-3][j],g[i+3&7][j]),g[i][j])for j in R]for i in R]


# p=lambda g:[[g[i][j]for j in range(8)]for i in range(8)]

# def p(g):
#  u=[s[:]for s in g]
#  for k in range(16):
#   if(j:=k//2)%3<2:
#    if g[i:=k&1][j]==g[i+6][j]>1:u[i+3][j]=g[i][j]
#    if g[j][i]==g[j][i+6]>1:u[j][i+3]=g[j][i]
#  return u

# def p(g):
#  u=[s[:]for s in g]
#  for i in range(2):
#   for j in range(8):
#    if j%3<2:
#     if g[i][j]==g[i+6][j]>1:u[i+3][j]=g[i][j]
#     if g[j][i]==g[j][i+6]>1:u[j][i+3]=g[j][i]
#  return u
