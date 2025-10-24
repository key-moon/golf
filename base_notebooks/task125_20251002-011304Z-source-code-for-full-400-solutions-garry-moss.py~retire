g=range
t=len
def p(r):
 r=[[8]+n+[8]for n in r];r=[[8]*len(r[0])]+r+[[8]*len(r[0])];d,d=t(r),t(r[0]);o=[-1,0,1];o=[[n,p]for n in o for p in o]
 for n in g(1,d-1):
  for p in g(1,d-1):
   if r[n][p]==8:
    c=[r[n+o][p+c]for(o,c)in o]
    if c.count(6)+c.count(4)>3:r[n][p]=4
 for n in g(1,d-1):
  for p in g(1,d-1):
   c=[r[n+o][p+c]for(o,c)in o]
   if r[n][p]==8and c.count(6)>0:r[n][p]=3
 r=[n[1:-1]for n in r[1:-1]];return r