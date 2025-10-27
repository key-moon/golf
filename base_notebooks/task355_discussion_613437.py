E=enumerate
M=max
p=lambda g:[[M(a:=[m for i,r in E(g)for j,v in E(r)if(m:=M(a:=r[M(0,j-3):j+4]+[s[j]for s in g[M(0,i-3):i+4]if s!=r],key=a.count))!=v],key=a.count)]]