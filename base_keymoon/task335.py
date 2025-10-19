# best: 107(4atj sisyphus luke Seek mukundan, Code Golf International) / others: 108(jailctf merger), 113(ox jam), 116(import itertools), 127(THUNDER THUNDER), 153(adakoda)
# ================================================== 107 ==================================================
# lambda g,c=-1,a=0:g*c or p([*zip(*[[(v or(c*6+8in s)*4)*(a|(a:=a^any(t)))for*t,v in zip(*g,s)]for s in g])],c+1)
p=lambda g,c=1,a=0:g*-c or p([[(v or(c*6+2in s)*4)*(a|(a:=a^any(t)))for t,v in zip(g,s)]for s in zip(*g)],c-1)
