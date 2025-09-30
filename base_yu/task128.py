# best: 59(jacekw Potatoman nauti natte) / others: 61(jailctf merger), 61(biz), 63(intgrah jimboko awu macaque sammyuri), 64(jacekwl Potatoman nauti), 64(4atj sisyphus luke Seek mukundan)
# =========================== 59 ==========================
# 34567890123456789012345678901234567890123456789012345678901234
# p=lambda g:[*map(list,zip(*[s[(k:=s[::-1].index(0)):]+s[:k]for s in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)]))]
# p=lambda g:[*zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)])]
p=lambda g:[*zip(*map(lambda*s:(s[-s.count(0):]+s)[:15],*g))]
# p=lambda g:[*zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)])]
# p=lambda g:[*map(list,zip(*[(s*2)[(k:=15-s.count(0)):k+15]for s in zip(*g)]))]
