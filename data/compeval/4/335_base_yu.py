# best: 126(jailctf merger) / others: 131(mukundan), 133(xsot ovs att joking mewheni), 143(4atj sisyphus luke Seek), 166(MasukenSamba), 174(dbdr)
# =========================================================== 126 ============================================================
p=lambda g,c=-1,E=enumerate:c*g or p([[s[j]or(2in s)+(8in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+2&4for j,t in E(zip(*g))]for i,s in E(g)],c+1)

