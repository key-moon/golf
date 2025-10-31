# best: 57(Code Golf International) / others: 59(FuunAgent), 63(jailctf merger), 63(ox jam), 65(HIMAGINE THE FUTURE.), 72(4atj sisyphus luke Seek mukundan)
# ========================== 57 =========================
# p=lambda g:sum([[[5]*11]+[sum([[5]+[v+5]*3for v in s[1::4]],[])[1:]]*3for s in g[1::4]],[])[1:]
# p=lambda g:sum([[sum([[5]+[v+5]*3for v in s[1::4]],[])[1:]]*3+g[3:4]for s in g[1::4]],[])[:7]
# p=lambda g:sum([[[5+s[i&12|(i%4<3)]for i in range(11)]]*3+g[3:4]for s in g[1::4]],[])[:7]
# p=lambda g:[[5+g[i&4|(i!=3)][j&12|(j%4<3)]for j in range(11)]for i in range(len(g))]
p=lambda g:[[5+s[j&12|(j%4<3)]for j in range(11)]for s in[g[1]]*3+g[4:5]+g[5:6]*3]


# p=lambda g:(s:=g[1])and[[5+s[i&12|(i%4<3)]for i in range(11)]]

# sum([[5]+[v+5]*3for v in s[1::4]],[])[1:]
# [5+s[i&12|(i%4<3)]for i in range(11)]
# p=lambda g:sum([[[5]*11]+[[*b"\5".join(bytes([v+5])*3for v in s[1::4])]]*3for s in g[1::4]],[])[1:]

# 1234 -> 6789
