# best: 122(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 207(jacekwl Potatoman nauti), 239(MasukenSamba), 256(J&R), 259(JRK), 260(jonas ryno kg583)
# ========================================================= 122 ==========================================================
def p(g):
 c=max(g)[0]
 k=g.index(max(g[3:6]))+1
 for _ in range(4):
#   g=[[((-~i%k)*(-~j%k)<1) and (v or 4) or (((i<k or {*g[i//k*k-1][j//k*k:][:k-1]}=={c}) and v<4 and 3 or 4))for j,v in enumerate(s)]for i,s in enumerate(g)]
#   g=[[((-~i%k)*(-~j%k)<1) and (v or 4) or (((i<k or {*g[i//k*k-1][j//k*k:][:k-1]}=={c}) and v<4 and 3 or 4))for j,v in enumerate(s)]for i,s in enumerate(g)]
  g=[[-~i%k*(-~j%k)<1and(v or 4)or 4-({*[[],*g][i//k*k][j//k*k:][:k-1]}<={c}!=4>v)for j,v in enumerate(s)]for i,s in enumerate(g)]
  g=[*zip(*g[::-1])]
 return g

# def p(g):
#  c=max(g)[0]
#  k=g.index(max(g[3:6]))
#  k2=k+1
#  for _ in range(4):
#   g=[[((-~i%k2)*(-~j%k2)<1) and (v==c and c or 4) or (i<k2 and (v or 3) or ({*g[i//k2*k2-1][j//k2*k2:][:k]}=={c} and (v<4 and 3 or 4) or 4))for j,v in enumerate(s)]for i,s in enumerate(g)]
#   g=[*map(list,zip(*g[::-1]))]
#  return g


# stripped:
# A=enumerate
# def p(g):
#  c=max(g)[0];k=g.index(max(g[3:6]))+1
#  for _ in range(4):g=[[-~i%k*(-~j%k)<1and(v or 4)or 4-({*[[],*g][i//k*k][j//k*k:][:k-1]}<={c}!=4>v)for(j,v)in A(s)]for(i,s)in A(g)];g=[*zip(*g[::-1])]
#  return g





