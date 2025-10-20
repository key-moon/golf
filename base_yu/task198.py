# best: 120(jacekw Potatoman nauti natte, import itertools) / others: 122(Code Golf International), 122(4atj sisyphus luke Seek mukundan), 122(jailctf merger), 122(ox jam), 124(JRKKX)
# ======================================================== 120 =========================================================
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
