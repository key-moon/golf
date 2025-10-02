# best: 220(4atj sisyphus luke Seek mukundan) / others: 222(jailctf merger), 228(jacekw Potatoman nauti natte), 228(ox jam), 229(jacekw Potatoman nauti), 244(natte)
def p(g):
 s,t=sorted(g)[-2:]
 S,T=sum(s),sum(t)
 if S<1:return[*map(list,zip(*p([*map(list,zip(*g))])))]
 t,z,s=s.index(S),g.index(s),g.index(t)
 if z>s:z,s=s,z;S,T=T,S
 while s>z+4:
  g[z][t]=S
  g[s][t]=T
  s-=1;z+=1
 g[z][t-2:t+3]=[S]*5;g[s][t-2:t+3]=[T]*5
#  g[i+1][c-2:c+3:4],g[j-1][c-2:c+3:4]=[S,S],[T,T]
#  a=g[i+1];a[c-2]=a[c+2]=S;a=g[j-1];a[c-2]=a[c+2]=T
#  a=i+1;g[a][c-2]=g[a][c+2]=S;a=j-1;g[a][c-2]=g[a][c+2]=T
 g[z+1][t-2]=g[z+1][t+2]=S;g[s-1][t-2]=g[s-1][t+2]=T
 return g
