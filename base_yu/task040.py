# best: 63(Code Golf International) / others: 69(jailctf merger), 69(ox jam), 70(4atj sisyphus luke Seek mukundan), 70(HIMAGINE THE FUTURE.), 72(import itertools)
# ============================= 63 ============================
# p=lambda g:[[g[i][j]and g[i>4 and 9][j>4 and 9]for j in range(10)]for i in range(10)]
# p=lambda g,E=enumerate:[[v and g[(i>4)*9][(j>4)*9]for j,v in E(s)]for i,s in E(g)]
# p=lambda g,R=range(10):[[g[i][j]and g[i>4and 9][j>4and 9]for j in R]for i in R]
# p=lambda g,R=range(10):[[g[i][j]and g[(i>4)*9][(j>4)*9]for j in R]for i in R]
# lambda g,R=range(10):[[g[i][j]and g[-(i>4)][-(j>4)]for j in R]for i in R]
# lambda g,h=[]:g*-1*-1or h*-1*-1or[p(g[i],(h+g)[(i>4)*9])for i in range(10)]
# lambda g,h=[]:g*-1*-1or h*-1*-1or[p(g[i],(h+g)[(i>4)*9])for i in range(10)]
# lambda g,h=[]:g and h if h*-1else[*map(p,g,(h+g)[:1]*5+(g+h)[-1:]*5)]
p=lambda g,h=[]:h*(0<g)if-1*h else[*map(p,g,(h+g)[:1]*5+(g+h)[-1:]*5)]
