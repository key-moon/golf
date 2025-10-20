# best: 105(Code Golf International, 4atj sisyphus luke Seek mukundan, ox jam, intgrah jimboko awu macaque sammyuri) / others: 106(jacekw Potatoman nauti natte), 106(import itertools), 106(Yuchen20), 107(natte), 108(jonas ryno kg583 kabutack)
# ================================================= 105 =================================================
# p=lambda g:(s:=[i for i,v in enumerate(sum(g,[]))if v],y:=min(i//(w:=len(g[0]))for i in s),x:=min(i%w for i in s))and[[g[y+i][x+j]&g[y+i%3*3][x+j%3*3]for j in range(9)]for i in range(9)]

# def p(g):
#  s,w=[i for i,v in enumerate(sum(g,[]))if v],len(g[0])
#  y,x=min(i//w for i in s),min(i%w for i in s)
#  return[[g[y+i][x+j]&g[y+i%3*3][x+j%3*3]for j in range(9)]for i in range(9)]

def p(g,R=range(9)):
 u=[[v for*t,v in zip(*g,s)if 5in t]for s in g if 5in s]
 return[[u[i][j]&u[i%3*3][j%3*3]for j in R]for i in R]

# p=lambda g,R=range(9):(u:=[[v for*t,v in zip(*g,s)if 5in t]for s in g if 5in s])and[[u[i][j]&u[i%3*3][j%3*3]for j in R]for i in R]
