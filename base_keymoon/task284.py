# best: 195(jailctf merger) / others: 204(ox jam), 205(Code Golf International), 217(ALE-Agent), 218(import itertools), 220(4atj sisyphus luke Seek mukundan)
# def p(g):
#  s,t=sorted(g)[-2:]
#  S,T=sum(s),sum(t)
#  if S<1:return[*map(list,zip(*p([*map(list,zip(*g))])))]
#  t,z,s=s.index(S),g.index(s),g.index(t)
#  if z>s:z,s=s,z;S,T=T,S
#  while s>z+4:
#   g[z][t]=S
#   g[s][t]=T
#   s-=1;z+=1
#  g[z][t-2:t+3]=[S]*5;g[s][t-2:t+3]=[T]*5
# #  g[i+1][c-2:c+3:4],g[j-1][c-2:c+3:4]=[S,S],[T,T]
# #  a=g[i+1];a[c-2]=a[c+2]=S;a=g[j-1];a[c-2]=a[c+2]=T
# #  a=i+1;g[a][c-2]=g[a][c+2]=S;a=j-1;g[a][c-2]=g[a][c+2]=T
#  g[z+1][t-2]=g[z+1][t+2]=S;g[s-1][t-2]=g[s-1][t+2]=T
#  return g

# def p(g):
#  u=[i for i in range(len(g)) if any(g[i])]
#  if len(u)<2:return [*zip(*p([*zip(*g)]))]
#  c=max(g[u[0]])
#  k=g[u[0]].index(c)
#  b=u[0]+u[-1]>>1
#  g[u[0]:b+1]=[[c*((i<1)*2<=abs(j-k)<=(i<2)*2) for j in range(len(g[0]))] for i in range(b+1-u[0])][::-1]
# #  g[u[0]:b]=[g[u[0]]]*(b-u[0])
# #  g[b-1]=[c*(k-2<=l<=k+2) for l in range(len(g[0]))]
# #  g[b]=[c*(l in (k-2,k+2)) for l in range(len(g[0]))]
#  return p(g[::-1]) if len(u)<3 else g[::-1]

# def p(g):
#  u=[i for i in range(len(g)) if any(g[i])]
#  if len(u)<2:return[*zip(*p([*zip(*g)]))]
#  b=u[0]+u[-1]>>1
#  return[[max(g[u[-(i>b)]])*((b-1<i<b+2)*2<=abs(j-g[u[0]].index(max(g[u[0]])))<=(b-2<i<b+3)*2)*(u[0]<=i<=u[-1]) for j in range(len(g[0]))]for i in range(len(g))]

p=lambda g:(len(u:=[i for i in range(len(g))if any(g[i])])>1)*[[max(g[u[-(i>u[0]+u[-1]>>1)]])*((u[0]+u[-1]>>1<=i<(u[0]+u[-1]>>1)+2)*2<=abs(j-g[u[0]].index(max(g[u[0]])))<=((u[0]+u[-1]>>1)-2<i<(u[0]+u[-1]>>1)+3)*2)*(u[0]<=i<=u[-1])for j in range(len(g[0]))]for i in range(len(g))]or[*zip(*p([*zip(*g)]))]
