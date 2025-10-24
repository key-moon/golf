def p(h):
 f=len(h)-1;n=[0]*16
 for u in range(f):
  for t in range(f):
   if(e:=h[u][t])and h[u+1][t]==e and h[u][t+1]==e:n[0]=n[4]=n[1]=e
   if e and h[u+1][t]==e and h[u+1][t+1]==e:n[8]=n[12]=n[13]=e
   if e and h[u][t+1]==e and h[u+1][t+1]==e:n[2]=n[3]=n[7]=e
   if(e:=h[u+1][t+1])and h[u+1][t]==e and h[u][t+1]==e:n[11]=n[14]=n[15]=e
 return[n[e:e+4]for e in(0,4,8,12)]