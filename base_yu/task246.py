# best: 105(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 114(import itertools), 127(THUNDER THUNDER), 144(biz), 152(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 153(adakoda)
# ================================================= 105 =================================================
p=lambda g,c=-1,E=enumerate:c*g or p([[s[j]or(2in s)+(3in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+6&8for j,t in E(zip(*g))]for i,s in E(g)],c+1)

# def p(g,E=enumerate):
#  for _ in 0,1:
# #   g=[[s[j] or ((2in s)+(3in t)+(0<sum(s[:j])<sum(s))+(0<sum(t[:i])<sum(t))+6)&8 for j,t in E(zip(*g))]for i,s in E(g)]
#   g=[[s[j]or(2in s)+(3in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+6&8for j,t in E(zip(*g))]for i,s in E(g)]
#  return g
