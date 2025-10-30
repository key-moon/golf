# best: 93(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 104(jacekw Potatoman nauti natte), 104(import itertools), 106(ox jam), 109(natte), 109(THUNDER THUNDER)
# ============================================ 93 ===========================================
p=lambda g,c=-3:c*g or p([[(y or(0<x%8<3)and(40//x%11))%(9+(c<0))for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# p=lambda g,c=-3:c*g or p([[(s[i]or(0<s[i-1]%8<3)and(40//s[i-1]%11))%(9+(c<0))for i in range(9)]for s in zip(*g[::-1])],c+1)
