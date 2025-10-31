# best: 104(Code Golf International) / others: 105(4atj sisyphus luke Seek mukundan), 105(jailctf merger), 105(ox jam), 108(HIMAGINE THE FUTURE.), 114(import itertools)
# ================================================ 104 =================================================
# lambda g,c=-1,a=0:g*c or p([*zip(*[[(v or(c+3in s)*8)*(a|(a:=a^any(t)))for*t,v in zip(*g,s)]for s in g])],c+1)
p=lambda g,c=1,a=0:g*-c or p([[(v or(c+2in s)*8)*(a|(a:=a^any(t)))for t,v in zip(g,s)]for s in zip(*g)],c-1)
