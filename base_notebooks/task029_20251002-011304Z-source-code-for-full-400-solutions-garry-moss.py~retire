def p(f,s=len,m=enumerate):
 for o in set(sum(f,[])):
  i=[[t,i]for(i,n)in m(f)for(t,n)in m(n)if n==o];n=sum(i,[]);t=n[::2];n=n[1::2];i=f[min(n):max(n)];i=[i[min(t)+1:max(t)][:]for i in i]
  if i[0].count(o)==s(i[0]):return i[1:]
 return f