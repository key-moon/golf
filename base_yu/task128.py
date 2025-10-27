# best: 59(jacekw Potatoman nauti natte, import itertools, jailctf merger) / others: 60(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 60(MasukenSamba), 60(JRKKX), 61(HIMAGINE THE FUTURE.), 61(biz)
# =========================== 59 ==========================
# 34567890123456789012345678901234567890123456789012345678901234
# p=lambda g:[*map(list,zip(*[s[(k:=s[::-1].index(0)):]+s[:k]for s in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)]))]
# p=lambda g:[*zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)])]
p=lambda g:[*zip(*map(lambda*s:(s[-s.count(0):]+s)[:15],*g))]
# p=lambda g:[*zip(*[(s[-s.count(0):]+s)[:15]for s in zip(*g)])]
# p=lambda g:[*map(list,zip(*[(s*2)[(k:=15-s.count(0)):k+15]for s in zip(*g)]))]
