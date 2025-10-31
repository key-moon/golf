# best: 59(ox jam) / others: 60(Code Golf International), 60(lv1.dev), 60(LogicLynx), 60(FuunAgent), 60(jailctf merger)
# =========================== 59 ==========================
# lambda g:[*zip(*[sorted(r,key=lambda x:x-1&3)for r in zip(*g)])]
# lambda g:[*zip(*[sorted(r,key=(1,2,0).index)for r in zip(*g)])]
# p=lambda g:[*zip(*[sorted(r,key=b"\0".find)for r in zip(*g)])]
p=lambda g:[*zip(*map(lambda*r:sorted(r,key=b"\0".find),*g))]
