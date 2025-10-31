# best: 124(ox jam) / others: 129(jailctf merger), 133(Code Golf International), 134(4atj sisyphus luke Seek mukundan), 138(FuunAgent), 138(THUNDER THUNDER)
# ========================================================== 124 ===========================================================
p=lambda g,c=-11,k=2:c*g or p(exec("d=0\nfor s in g:d+=s[0]>1;s[d:]=g[0]"*(f:=8in g[0]and max(g)[0]==k))or[*map(list,zip(*g[::1-c%3|1]))],c+1,k+f)

# def p(g):
#  k=2
#  for c in range(-11,1):
#   if 8in g[0]and max(g)[0]==k:
#    d,k=0,99
#    for s in g:
#     d+=s[0]>>1
#     s[d:]=g[0]
#   *g,=map(list,zip(*g[::1-c%3|1]))
#  return g


# def p(g):
#  k=2
#  for c in range(-11,1):
#   if 8in g[0]and max(g)[0]==k:
#    d,k=0,99
#   #  for s in g:
#   #   d+=s[0]>>1
#   #   s[d:]=g[0]
#    exec("for s in g:d+=s[0]>>1;s[d:]=g[0]")
#   *g,=map(list,zip(*g[::1-c%3|1]))
#  return g
