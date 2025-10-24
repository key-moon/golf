def p(r,l=enumerate):
 t=len(r[0]);t=[-1]+[t for(t,a)in l(zip(*r))if not any(a)]+[t];a=[[n[t[a]+1:t[a+1]]for n in r]for a in range(len(t)-1)if t[a]+1<t[a+1]];n=a[:1]
 for u in a[1:]:t=n[-1];t=next((a for(a,t)in l(t)if t and t[-1]==5),0);r=next((a for(a,t)in l(u)if t and t[0]==5),0);r=t-r;t=[[0]*len(u[0])]*3;n+=[(t+u+t)[3-r:6-r]]
 t=[next((t for a in t for t in a if t>0and t!=5),0)for t in a];r=[[[a if t==5else t for t in t]for t in t]for(t,a)in zip(n,t)];return[sum(t,[])for t in zip(*r)]