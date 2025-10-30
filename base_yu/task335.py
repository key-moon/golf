# best: 107(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 110(HIMAGINE THE FUTURE.), 113(ox jam), 115(import itertools), 127(THUNDER THUNDER), 146(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ================================================== 107 ==================================================
p=lambda g,c=-1,E=enumerate:c*g or p([[s[j]or(2in s)+(8in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+2&4for j,t in E(zip(*g))]for i,s in E(g)],c+1)
