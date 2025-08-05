R=range
def p(g):
 h,w=len(g),len(g[0])
#  s=[i for i,v in enumerate(sum(g,[]))if v]
#  s=[i for i in range(h*w)if g[i%h][i//h]]
#  s=sum([[i,j]for I in R(h*w)if g[i:=I%h][j:=I//h]],[])
 s=sum([[i,j]for i in R(h)for j in R(w)if g[i][j]],[])
#  return[[[g[s[0]][s[1]],g[i][j]][max(abs(i-s[2]),abs(j-s[3]))%(s[3]-s[1])>0]for j in range(w)]for i in range(h)]
 return[[[g[i][j],g[s[0]][s[1]]][max(abs(i-s[2]),abs(j-s[3]))%(s[3]-s[1])==0]for j in R(w)]for i in R(h)]

# def p(g):
#  h,w=len(g),len(g[0])
# #  s=[i for i,v in enumerate(sum(g,[]))if v]
# #  s=[i for i in range(h*w)if g[i%h][i//h]]
#  s=sum([[i,j] for i in range(h) for j in range(w)if g[i][j]],[])
#  for i in range(h):
#   for j in range(w):
#    if max(abs(i-s[2]),abs(j-s[3]))%(s[3]-s[1])==0:
#     g[i][j]=g[s[0]][s[1]]
#  return g