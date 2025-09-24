# best: 93(4atj sisyphus luke Seek mukundan) / others: 97(jailctf merger), 106(ox jam), 109(natte), 117(jacekw Potatoman nauti), 117(2F)
# ============================================ 93 ===========================================
p=lambda g,c=-3:c*g or p([[(y or(0<x%8<3)and(40//x%11))%(9+(c<0))for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# p=lambda g,c=-3:c*g or p([[(s[i]or(0<s[i-1]%8<3)and(40//s[i-1]%11))%(9+(c<0))for i in range(9)]for s in zip(*g[::-1])],c+1)
