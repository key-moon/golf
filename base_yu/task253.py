# best: 129(4atj sisyphus luke Seek mukundan) / others: 148(xsot ovs att joking mewheni), 151(4atj sisyphus luke Seek), 153(natte), 161(jailctf merger), 172(kg583)
# ============================================================= 129 =============================================================
# port re;t=r"([^0]), \1.{%s}\1";u=r"([^0]).{%s}\1, \1";P=[t%37,t%40,u%40,u%37]*2+["(0)"]*4;p=lambda g:[[int(re.search(P[i+j],str(g))[1])for j in(0,4,5,1)]for i in(0,4,6,2)]
# port re;Z="([1-9])";A=Z+r".{%s}\1";t=Z+".."+A;u=A+".."+Z;P=[t%37,t%40,u%40,u%37]*2+["(0)"]*4;p=lambda g:[[int(re.search(P[i+j],str(g))[1])for j in(0,4,5,1)]for i in(0,4,6,2)]
# port re;Z="..([1-9])";A=Z+".{%s}\\1";t=Z+A;u=A+Z;P=[t%37,t%40,u%40,u%37]*2+["(0)"]*4;p=lambda g:[[int(re.search(P[i+j],str(g))[1])for j in(0,4,5,1)]for i in(0,4,6,2)]
import re;Z="..([1-9])";A=Z+".{%s}\\1";t=Z+A;u=A+Z;P=[t%37,t%40,u%40,u%37]*2+["(0)"]*4;p=lambda g:[[int(re.search(P[i+j],str(g))[1])for j in(0,4,5,1)]for i in(0,4,6,2)]


# def p(g,R=range(12)):
#  _,(a,b,c,d)=zip(*sorted([(u.index(0),max(u))for i in R for j in R if sum(u:=g[i][j:j+2]+g[i+1][j:j+2])>max(u)*2]))
#  return[[d,d,c,c],[d,0,0,c],[b,0,0,a],[b,b,a,a]]

# def p(g,R=range(12)):
#  u=sorted([u for i in R for j in R if sum(u:=g[i][j:j+2]+g[i+1][j:j+2])>max(u)*2],key=lambda u:u.index(0))
# #  return[u[3][:2]+u[2][:2],u[3][2:]+u[2][2:],u[1][:2]+u[0][:2],u[1][2:]+u[0][2:]]
#  return[u[a][c:c+2]+u[b][c:c+2]for a,b,c in((3,2,0),(3,2,2),(1,0,0),(1,0,2))]

# def p(g):
#  *o,=eval("[0]*4,"*4)
#  for _ in range(4):
#   for i in range(12):
#    for j in range(12):
#     if g[i][j]==g[i+1][j]==g[i][j+1]>0:
#      o[0][0]=o[0][1]=o[1][0]=g[i][j]
#   *g,=zip(*g[::-1])
#   *o,=map(list,zip(*o[::-1]))
#  return o
