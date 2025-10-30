# best: 60(jailctf merger) / others: 61(jacekwl Potatoman nauti), 61(jacekw Potatoman nauti natte), 61(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 61(JRKX), 61(Code Golf International)
# =========================== 60 ===========================
# lambda g:[*zip(*[sorted(r,key=lambda x:x-1&3)for r in zip(*g)])]
# lambda g:[*zip(*[sorted(r,key=(1,2,0).index)for r in zip(*g)])]
# p=lambda g:[*zip(*[sorted(r,key=b"\0".find)for r in zip(*g)])]
p=lambda g:[*zip(*map(lambda*r:sorted(r,key=b"\0".find),*g))]
