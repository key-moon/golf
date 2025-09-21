# best: 61(biz) / others: 64(ox jam), 64(4atj sisyphus luke Seek mukundan), 64(jacekw Potatoman nauti), 64(jailctf merger), 64(intgrah jimboko awu macaque sammyuri)
# ============================ 61 ===========================
# 34567890123456789012345678901234567890123456789012345678901234
# p=lambda g:[*map(list,zip(*[s[(k:=s[::-1].index(0)):]+s[:k]for s in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)]))]
# p=lambda g:[*zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)])]
p=lambda g:[*zip(*map(lambda*s:(s[-s.count(0):]+s)[:15],*g))]
# p=lambda g:[*zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)])]
# p=lambda g:[*map(list,zip(*[(s*2)[(k:=15-s.count(0)):k+15]for s in zip(*g)]))]
