t=enumerate
m=len
def p(s):
 r=sum(s,[]);i=sorted([[r.count(s),s]for s in set(r)if s>0]);e=[[e,s]for(s,r)in t(s)for(e,r)in t(r)if r==i[-1][1]];r=sum(e,[]);e=r[::2];r=r[1::2];s=s[min(r):max(r)+1];s=[s[min(e):max(e)+1][:]for s in s]
 if m(s)<3:
  if s[0].count(0)>0:s=[[0,0,0]]+s
  else:s=s+[[0,0,0]]
 if m(s[0])<3:
  if[s[0][0],s[1][0],s[2][0]].count(0)>0:s=[[0]+s for s in s]
  else:s=[s+[0]for s in s]
 s=[[i[0][1]if s==0else s for s in s]for s in s];return s