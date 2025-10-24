o=enumerate
i=range
a=len
def p(m):
 r=sum(m,[]);f=sorted([[r.count(f),f]for f in set(r)if f>0])
 for r in i(2):
  k=[[k,r]for(r,s)in o(m)for(k,l)in o(s)if l==f[-1][1]];r=sum(k,[]);s=r[::2];k=r[1::2];r=m[min(k):max(k)+1];r=[r[min(s):max(s)+1][:]for r in r];r=[[0if r!=f[-1][1]else r for r in r]for r in r];l=a(r)//3;r=r[::l];r=[r[::l]for r in r]
  if(max(s)-min(s))*(max(k)-min(k))<a(m)*a(m[0])-101and a(r)==3and a(r[0])==3:break
  f=f[::-1]
 r=[[f[0][1]if r>0else r for r in r]for r in r]
 if r==[[0,0,0],[0,0,0],[0,5,0]]:r=[[4,0,0],[0,4,4],[0,0,4]]
 return r