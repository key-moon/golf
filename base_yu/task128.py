# best: 64(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri, HETHAT, xsot ovs att joking mewheni, mukundan) / others: 69(natte), 71(jonas ryno kg583), 74(duckyluuk), 74(kg583), 74(JRK)
# ============================= 64 =============================
# 34567890123456789012345678901234567890123456789012345678901234
# p=lambda g:[*map(list,zip(*[s[(k:=s[::-1].index(0)):]+s[:k]for s in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)]))]
p=lambda g:[*zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)])]
# p=lambda g:[*zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)])]
# p=lambda g:[*map(list,zip(*[(s*2)[(k:=15-s.count(0)):k+15]for s in zip(*g)]))]
