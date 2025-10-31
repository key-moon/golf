# best: 105(jailctf merger) / others: 106(Code Golf International), 107(4atj sisyphus luke Seek mukundan), 110(HIMAGINE THE FUTURE.), 110(ox jam), 115(import itertools)
# ================================================= 105 =================================================
# lambda g,c=-1,a=0:g*c or p([*zip(*[[(v or(c*6+8in s)*4)*(a|(a:=a^any(t)))for*t,v in zip(*g,s)]for s in g])],c+1)
p=lambda g,c=1,a=0:g*-c or p([[(v or(c*6+2in s)*4)*(a|(a:=a^any(t)))for t,v in zip(g,s)]for s in zip(*g)],c-1)
