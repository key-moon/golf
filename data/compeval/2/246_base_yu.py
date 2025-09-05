# best: 126(jailctf merger) / others: 131(xsot ovs att joking mewheni), 143(4atj sisyphus luke Seek), 170(natte), 194(Potatoman), 195(MasukenSamba)
# =========================================================== 126 ============================================================
p=lambda g,c=-1,E=enumerate:c*g or p([[s[j]or(2in s)+(3in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+6&8for j,t in E(zip(*g))]for i,s in E(g)],c+1)

# def p(g,E=enumerate):
#  for _ in 0,1:
# #   g=[[s[j] or ((2in s)+(3in t)+(0<sum(s[:j])<sum(s))+(0<sum(t[:i])<sum(t))+6)&8 for j,t in E(zip(*g))]for i,s in E(g)]
#   g=[[s[j]or(2in s)+(3in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+6&8for j,t in E(zip(*g))]for i,s in E(g)]
#  return g
