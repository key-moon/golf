# best: 80(luke, kabutack) / others: 81(biz), 84(natte), 85(joking+MWI), 85(mukundan), 85(joking)
# 多分70までは縮むはず
# lambda g:[*zip(*[[s,s[:-(s.count(2)//2)]+99*(8,)][any(s)]for s in zip(*g)])] <- zipのclipを利用しようとした残骸
# lambda g:[*zip(*[s[:len(s)-(u:=s.count(2)//2)]+u*(8,)for s in zip(*g)])]
# ===================================== 80 =====================================
p=lambda g:[*zip(*[s[:-(u:=s.count(2)//2)or 99]+u*(8,)for s in zip(*g)])]

