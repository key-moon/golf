# best: 53(Code Golf International, HIMAGINE THE FUTURE.) / others: 55(LogicLynx), 57(FuunAgent), 59(jailctf merger), 63(ox jam), 64(4atj sisyphus luke Seek mukundan)
# ======================== 53 =======================
# 3456789012345678901234567890123456789012345678901234567890123456789012
# p=lambda g:[g[:(h:=len(g)//2)],[s[:(w:=len(s)//2)]for s in g]][g[0]!=g[h]or h<w]
# p=lambda g:[g[:(h:=len(g)//2)],[s[:(w:=len(g[0])//2)]for s in g]][g[0]!=g[h]]
# p=lambda g:(g==(a:=g[:53%~-len(g)])*2)*a or[*map(p,g)]
p=lambda g:(a:=g[:53%~-len(g)])*(g==a*2)or[*map(p,g)]
