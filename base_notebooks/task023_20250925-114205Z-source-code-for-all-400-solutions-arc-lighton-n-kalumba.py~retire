def p(g):
 G={(r,c)for r,row in enumerate(g)for c,v in enumerate(row)if v}
 while G:
  M={c:[]for c in G}
  for i in range(3):
   for r in range(11):
    for c in range(11):
     Q={(r+[j//2,j,0][i],c+[j%2,0,j][i])for j in range((4,3,3)[i])}
     if Q<=G:[M[x].append(Q)for x in Q]
  c=min(G,key=lambda c:len(M[c]));Q=M[c][0];G-=Q
  for x,y in Q:g[x][y]=(len(Q)-3)*6+2
 return g
