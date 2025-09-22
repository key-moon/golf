# best: 106(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 107(4atj sisyphus luke Seek mukundan), 127(natte), 184(jacekw Potatoman nauti), 203(MasukenSamba), 206(kdmitrie)
# ================================================= 106 ==================================================

# p=lambda g,R=range(12):((g[6][0]==2)and(a:=g[0].count(2))and[[g[i][j]or(abs(i-(1|(d:=-(8in g[-1])))*(g[d].index(8)-a)%11)+a==j)*3 for j in R]for i in R])or[*zip(*p([*zip(*g[::-1])]))][::-1]

# def p(g):
#  for _ in range(4):
#   if g[6][0]==2:
#    a=g[0].count(2)
#    g=[[g[i][j]or(abs(i-(1|(d:=-(8in g[-1])))*(g[d].index(8)-a)%11)+a==j)*3 for j in range(12)]for i in range(12)]
#   g=[*zip(*g[::-1])]
#  return g

# def p(g):
#  for _ in range(4):
#   if g[6][0]==2:
#    a=g[0].count(2)
#    d=8in g[-1]
#    b=g[-d].index(8)
#    g=[[g[i][j]or(abs(i-(1|-d)*(b-a)%11)+a==j)*3 for j in range(12)]for i in range(12)]
#   g=[*zip(*g[::-1])]
#  return g

# def p(g,R=range(12)):
#  for d in range(60):
#   g=[[g[i][j]or(i>1<j and g[i-1][j-1]>2<g[i-(g[i-2][j-2]!=2)*2][j-2])*3for j in R]for i in R]
#   g=[*zip(*g[::1-d%3|1])]
#  return g

# lambda g,c=-59,R=range(12):c*g or p([*zip(*[[g[i][j]or(i>1<j and g[i-1][j-1]>2<g[i-(g[i-2][j-2]!=2)*2][j-2])*3for j in R]for i in R][::1-c%3|1])],c+1)


# def p(g):
#  for I in range(4800):
#   u,v=I%2*2-1,(I&2)-1
#   if g[i:=I//40%10+1][j:=I//4%10+1]>2and g[i+u][j+v]>2:
#    s=g[i+u*~-(g[i-u][j]&2)]
#    s[w]=s[w:=j+v*~-(g[i][j-v]&2)]or 3
#  return g

# def p(g):
#  for _ in range(12):
#   for i in range(1,11):
#    for j in range(1,11):
#     for k in range(4):
#      u=k%2*2-1
#      v=(k&2)-1
#      if g[i][j]>2 and g[i+u][j+v]>2:
#       s=g[i+u*~-(g[i-u][j]&2)]
#       s[w]=s[w:=j+v*~-(g[i][j-v]&2)] or 3
#  return g

# ================================================= 106 ==================================================
# import re;p=lambda g,c=-59:g*c or eval(re.sub("0(?=.{40}[38].{40}[238])","3",str([*zip(*p(g,c+1))][::1-c%3|1])))
import re;p=lambda g,c=-59:g*c or[*zip(*eval(re.sub("0(?=.{40}[38].{40}[238])","3",str(p(g,c+1)))))][::1-c%3|1]