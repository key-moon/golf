# best: 151(Code Golf International) / others: 153(ox jam), 155(jailctf merger), 163(LogicLynx), 163(FuunAgent), 167(4atj sisyphus luke Seek mukundan)
def p(g):
 R=range(11)
#  t=[sorted(sum([s[j&12:][:3]for s in g[i&12:][:3]],[]))for i in R for j in R]
 t=[sorted(sum([*zip(*g[i&12:][:3])][j&12:][:3],()))for i in R for j in R]
 m=max(t)
 return[[(g[i][j]==5)*5or(t[i*11+j]==m)*m[8]for j in R]for i in R]

# def p(g):
#  R=(0,4,8)
#  S=range(11)
#  t=[sum(sum([s[j:j+3]for s in g[i:i+3]],[]))for i in R for j in R]
#  return[[(g[i][j]==5)*5or(t[i//4*3+j//4]==max(t))*(sum({*sum(g,[])})-5)for j in S]for i in S]
# #  t=[sum([s[j:j+3]for s in g[i:i+3]],[])for i in R for j in R]
# #  return[[(g[i][j]==5)*5or(sum(t[i//4*3+j//4])==max(map(sum,t)))*max(max(t))for j in S]for i in S]
