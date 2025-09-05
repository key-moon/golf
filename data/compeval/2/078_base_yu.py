# best: 61(joking+MWI) / others: 65(ovs), 65(luke), 65(4atj), 71(joking), 72(mukundan)
# ============================ 61 ===========================
# lambda g:[*zip(*[sorted(r,key=lambda x:x-1&3)for r in zip(*g)])]
# lambda g:[*zip(*[sorted(r,key=(1,2,0).index)for r in zip(*g)])]
p=lambda g:[*zip(*[sorted(r,key=b"\0".find)for r in zip(*g)])]
