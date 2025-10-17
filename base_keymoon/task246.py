# best: 105(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 114(import itertools), 127(THUNDER THUNDER), 144(biz), 153(adakoda), 154(jacekw Potatoman nauti natte)
# ================================================= 105 =================================================
# lambda g,c=-1,a=0:g*c or p([*zip(*[[(v or(c+3in s)*8)*(a|(a:=a^any(t)))for*t,v in zip(*g,s)]for s in g])],c+1)
p=lambda g,c=1,a=0:g*-c or p([[(v or(c+2in s)*8)*(a|(a:=a^any(t)))for t,v in zip(g,s)]for s in zip(*g)],c-1)
