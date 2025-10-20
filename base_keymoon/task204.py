# best: 93(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 106(intgrah jimboko awu macaque sammyuri), 110(2F), 110(biz), 128(import itertools), 151(ShadowPrompt Labs)
# ============================================ 93 ===========================================
# 302の丸コピ
p=lambda g:[(D:=0)or[int(D:=r.pop(0)and(D<1)/2+1or D>1and[7-r.index(1)%2*5,D][2<=D])for _ in g]for r in g]
