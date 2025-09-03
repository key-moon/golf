# best: 109(4atj sisyphus luke Seek) / others: 127(mukundan), 188(xsot ovs att joking mewheni), 196(jailctf merger), 211(MasukenSamba), 240(Potatoman)
# =================================================== 109 ===================================================
# flattenで縦方向を見る
# f p(g):S=sum(g,[]);a=max([[[*t][1]for i in range(len(S))if len(t:={0,*S[i%j::j]})==2]for j in range(30,300)],key=len);return[*zip(*[iter(a)]*29)]
# lambda g:[*zip(*[max([[[*t][1]for i in range(len(s))if len(t:={0,*s[i%j::j]})==2]for j in b"\5\6\7\10\11"],key=len)for s in zip(*g)])]
p=lambda g:[max([[[*t][1]for i in range(len(s))if len(t:={0,*sum(g,[])[i%j::j]})==2]for j in b"\5\6\7\10\11\12\13\14"],key=len)for s in g]
p=lambda g:(S:=sum(g,[]))and[max([[[*t][1]for i in range(len(s))if len(t:={0,*sum(g,[])[i%j::j]})==2]for j in b"\5\6\7\10\11\12\13\14"],key=len)for s in g]


