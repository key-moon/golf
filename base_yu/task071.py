# best: 122(jailctf merger) / others: 135(4atj sisyphus luke Seek), 182(jacekwl), 187(jacekw), 224(Potatoman), 235(xsot ovs att joking mewheni)
# ========================================================= 122 ==========================================================
def p(g):
 c=[*filter(int,sum(g,[]))][0]
 for p in range(32):
  x=[[{s[j],(s+g[0])[p-j]}&{0,c}for j in range(16)]for s in g]
  if{0,c}>max(max(x)):
   return[[*map(sum,s)]for s in x]
   

# R=range
# def p(g):
#  c=[v for v in sum(g,[])if v][0]
#  for p in R(32):
#   if all((0<=p-j<16)and g[i][p-j]for I in R(256)if g[i:=I%16][j:=I>>4]==c):
#    return [[~(g[i][j]not in(0,c)and~g[i][p-j]or~g[i][j])for j in R(16)]for i in R(16)]
