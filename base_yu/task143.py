# best: 137(xsot ovs att joking mewheni) / others: 140(jailctf merger), 158(4atj sisyphus luke Seek mukundan), 158(4atj sisyphus luke Seek), 194(mukundan), 250(jacekwl Potatoman)
# ================================================================= 137 =================================================================

# p=lambda g,R=range(10):[[((f:=[(t:=[i for i in range(100)if g[i//10][i%10]==c])and[v-min(t)for v in t]for c in R]).count(f[v:=g[i][j]])>1<4<i+j)*5or v for j in R]for i in R]

# def p(g,R=range(10)):
#  f=[(t:=[i for i in range(100)if g[i//10][i%10]==c])and[v-min(t)for v in t]for c in R]
#  return[[(f.count(f[v:=g[i][j]])>1<4<i+j)*5or v for j in R]for i in R]

p=lambda g:[[((f:=lambda c:(t:=[i for i in range(100)if g[i//10][i%10]==c])and[v-min(t)for v in t])(v)==f(c:=max(g[0][:3]+g[1][:3]))!=v!=c)*5or v for v in s]for s in g]

# def p(g):
#  f=lambda c:(t:=[i for i in range(100)if g[i//10][i%10]==c])and[v-min(t)for v in t]
#  return[[(f(v)==f(c:=max(g[0][:3]+g[1][:3]))!=v!=c)*5or v for v in s]for s in g]

# def p(g):
#  f=[(t:=[i for i in range(100)if g[i//10][i%10]==c])and[v-min(t)for v in t]for c in range(10)]
#  c=max(g[0][:3]+g[1][:3])
#  return[[(f[v]==f[c]!=v!=c)*5or v for v in s]for s in g]

# def p(g):
#  f=[[i for i in range(100)if g[i//10][i%10]==c]for c in range(10)]
#  c=max(g[0][:3]+g[1][:3])
#  return [[(len({x-y for x,y in zip(f[c],f[v])})==1 and len(f[c])==len(f[v]) and v!=c)*5 or v for v in s]for s in g]

# def p(g):
#  f=[[i for i in range(100)if g[i//10][i%10]==c+1]for c in range(9)]
#  c=max(g[0][:3]+g[1][:3])-1
#  for i in range(9):
#   if len({x-y for x,y in zip(f[c],f[i])})==1 and len(f[c])==len(f[i]) and i!=c:
#    for k in f[i]:
#     g[k//10][k%10]=5
#  return g
