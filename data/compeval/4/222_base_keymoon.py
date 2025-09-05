# best: 106(xsot ovs att joking mewheni) / others: 114(4atj sisyphus luke Seek), 144(natte), 171(mukundan), 182(jailctf merger), 233(jacekw)
# ================================================= 106 ==================================================
# lambda g:[*zip(*zip([[c for c in r if c==max(g)]for r in g]))]
# port re;p=lambda g,c=-99:g*c or eval(re.sub(r"([^0])(?=, \1.{46}\1, \1)","0",str(p(g,c+1))))
p=lambda g,E=enumerate:[[t[i]*(t[i]<sum([0,*t][i:i+3]+[0,*s][j:j+3]))for j,t in E(zip(*g))]for i,s in E(g)]
