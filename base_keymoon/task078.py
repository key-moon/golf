# best: 60(jailctf merger) / others: 61(jacekwl Potatoman nauti), 61(jacekw Potatoman nauti natte), 61(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 61(JRKX), 61(Code Golf International)
# =========================== 60 ===========================

# p=lambda g:[*map(list,zip(*[[*r[:(a:=r.index(0))]]+sorted(r[a:])[::-1]for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[[1]*(c:=r.count)(1)+[2]*c(2)+[0]*c(0)for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:"201"[x])for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:(x-1)%3)for r in zip(*g)]))]
# ===============================================================12345678901
p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:x-1&3)for r in zip(*g)]))]
