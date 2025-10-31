# best: 59(ox jam) / others: 60(Code Golf International), 60(lv1.dev), 60(LogicLynx), 60(FuunAgent), 60(jailctf merger)
# =========================== 59 ==========================

# p=lambda g:[*map(list,zip(*[[*r[:(a:=r.index(0))]]+sorted(r[a:])[::-1]for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[[1]*(c:=r.count)(1)+[2]*c(2)+[0]*c(0)for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:"201"[x])for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:(x-1)%3)for r in zip(*g)]))]
# ===============================================================12345678901
p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:x-1&3)for r in zip(*g)]))]
