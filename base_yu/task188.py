# best: 61(jailctf merger) / others: 64(4atj sisyphus luke Seek mukundan), 68(ox jam), 74(jacekw Potatoman nauti), 74(jacekwl Potatoman nauti), 75(xsot ovs att joking mewheni)
# ============================ 61 ===========================
# 3456789012345678901234567890123456789012345678901234567890123456789012
# p=lambda g:[g[:(h:=len(g)//2)],[s[:(w:=len(s)//2)]for s in g]][g[0]!=g[h]or h<w]
# p=lambda g:[g[:(h:=len(g)//2)],[s[:(w:=len(g[0])//2)]for s in g]][g[0]!=g[h]]
# p=lambda g:(g==(a:=g[:53%~-len(g)])*2)*a or[*map(p,g)]
p=lambda g:(a:=g[:53%~-len(g)])*(g==a*2)or[*map(p,g)]
