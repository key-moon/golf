def p(g):
 s,t=sorted(g)[-2:];A,B=sum(s),sum(t)
 if A<1:return[*map(list,zip(*p([*map(list,zip(*g))])))]
 t,z,s=s.index(A),g.index(s),g.index(t)
 if z>s:z,s=s,z;A,B=B,A
 while s>z+4:g[z][t]=A;g[s][t]=B;s-=1;z+=1
 g[z][t-2:t+3]=[A]*5;g[s][t-2:t+3]=[B]*5;g[z+1][t-2]=g[z+1][t+2]=A;g[s-1][t-2]=g[s-1][t+2]=B;return g