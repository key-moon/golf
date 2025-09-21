# best: 136(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 139(4atj sisyphus luke Seek mukundan), 156(natte), 160(jacekw Potatoman nauti), 160(jacekwl Potatoman nauti), 184(MasukenSamba)
# ================================================================ 136 =================================================================
# p=lambda g:[*zip(*[(f:=0,t:=[*s])and[(c:=max(max(g[::-1],key=any)))*(f:=f or{*s}>{*t}>{c})|t.pop(0)for _ in s]for s in zip(*g)])]
# p=lambda g:[*zip(*[(f:=0)or[s[i]|(c:=max(max(g[::-1],key=any)))*(f:=f or{*s}>{*s[i:]}>{c})for i in range(20)]for s in zip(*g)])]
p=lambda g:[*zip(*map(lambda*s:(f:=0)or[s[i]|(c:=max(max(g[::-1],key=any)))*(f:=f or{*s}>{*s[i:]}>{c})for i in range(20)],*g))]

# def p(g):
#  c=max(max(g[::-1],key=any))
#  return[*zip(*[(f:=0)or[(f:=f or{*s}>{*s[i:]}>{c})*c|s[i]for i in range(20)]for s in zip(*g)])]

# def p(g):
#  c=max(max(g[::-1],key=any))
#  g=[*map(list,zip(*g))]
#  for s in g:
#   for i in range(20):
#    if {*s}>{*s[i:]}>{c}:
#     s[i:]=[c]*99
#  g=[*zip(*g)]
#  return g

# R=range
# def p(g):
#  c=[next(filter(int,s))for s in g if any(s)][-1]
#  for I in R(400):
#   for k in R(i:=I%20,0,-1):
#    if c==g[i][j:=I//20]!=g[k][j]>0:
#     for s in g[k+1:20]:s[j]=g[i][j]
#     break
#  return g

# def p(g):
#  c=[next(filter(int,s))for s in g if any(s)][-1]
#  for i in range(20):
#   for j in range(20):
#    for k in range(i)[::-1]:
#     if c==g[i][j]!=g[k][j]>0:
#      for l in range(k+1,20):g[l][j]=g[i][j]
#      break
#  return g
