# best: 109(4atj sisyphus luke Seek mukundan, biz, jailctf merger, xsot ovs att joking mewheni) / others: 116(natte), 123(kabutack), 126(HETHAT), 142(MasukenSamba), 147(duckyluuk)
# =================================================== 109 ===================================================
# p=lambda g,E=enumerate:[[s[j]or sum(({*s[:j]}&{*s[j:]})-{0,g[0][2]}) or sum(({*t[:i]}&{*t[i:]})-{0,g[0][2]}) for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or sum(({*s[:j:3]}&{*s[j::3]}|{*t[:i:3]}&{*t[i::3]}))for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[s[j]|sum({*s[:j:3]}&{*s[j::3]}|{*t[:i:3]}&{*t[i::3]})for j,t in E(zip(*g))]for i,s in E(g)]

