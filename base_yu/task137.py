# best: 137(jailctf merger) / others: 141(ox jam), 143(import itertools), 144(natte), 144(jacekw Potatoman nauti natte), 146(THUNDER THUNDER)
# ================================================================= 137 =================================================================
# def p(g):
#  R=range(len(g))
#  x,y,_=[i for i in R if[*map(max,*g)][i]]
#  return[[(max(abs(i-g.index(max(g,key=any))-y+x),abs(j-y))%(y-x)==0)*max(max(g))for j in R]for i in R]

def p(g,R=range):
 w=len(g)
 x,y,_=[i for i in R(w*w)if g[i//w][i%w]]
 return[[(max(abs(i-y//w),abs(j-y%w))%(y%w-x%w)==0)*max(max(g))for j in R(w)]for i in R(w)]

# def p(g,E=enumerate):
#  w=len(g)
#  x,y,_=[i for i,v in E(sum(g,[]))if v]
#  return[[(max(abs(i-y//w),abs(j-y%w))%(y%w-x%w)==0)*max(max(g))for j,v in E(s)]for i,s in E(g)]


# R=range
# def p(g):
#  h,w=len(g),len(g[0])
#  s=sum([[I%h,I//h]for I in R(h*w)if g[I%h][I//h]],[])
#  return[[(max(abs(i-s[2]),abs(j-s[3]))%(s[3]-s[1])==0)*max(max(g))for j in R(w)]for i in R(h)]

# R=range
# def p(g):
#  h,w=len(g),len(g[0])
# #  s=[i for i,v in enumerate(sum(g,[]))if v]
# #  s=[i for i in range(h*w)if g[i%h][i//h]]
# #  s=sum([[i,j]for I in R(h*w)if g[i:=I%h][j:=I//h]],[])
#  s=sum([[i,j]for i in R(h)for j in R(w)if g[i][j]],[])
# #  return[[[g[s[0]][s[1]],g[i][j]][max(abs(i-s[2]),abs(j-s[3]))%(s[3]-s[1])>0]for j in range(w)]for i in range(h)]
#  return[[[g[i][j],g[s[0]][s[1]]][max(abs(i-s[2]),abs(j-s[3]))%(s[3]-s[1])==0]for j in R(w)]for i in R(h)]

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
