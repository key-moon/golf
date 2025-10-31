# best: 105(jailctf merger) / others: 106(Code Golf International), 107(4atj sisyphus luke Seek mukundan), 110(HIMAGINE THE FUTURE.), 110(ox jam), 115(import itertools)
# ================================================= 105 =================================================
p=lambda g,c=-1,E=enumerate:c*g or p([[s[j]or(2in s)+(8in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+2&4for j,t in E(zip(*g))]for i,s in E(g)],c+1)
