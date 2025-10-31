# best: 65(Code Golf International) / others: 66(LogicLynx), 66(jailctf merger), 66(HIMAGINE THE FUTURE.), 66(ox jam), 66(intgrah jimboko awu macaque sammyuri)
# 多分70までは縮むはず
# lambda g:[*zip(*[[s,s[:-(s.count(2)//2)]+99*(8,)][any(s)]for s in zip(*g)])] <- zipのclipを利用しようとした残骸
# lambda g:[*zip(*[s[:len(s)-(u:=s.count(2)//2)]+u*(8,)for s in zip(*g)])]
# ============================== 65 =============================
# lambda g:[*zip(*[s[:-(u:=s.count(2)//2)or 99]+u*(8,)for s in zip(*g)])]
# lambda g:[*zip(*[s[:-(u:=sum(s)//4)or 99]+u*(8,)for s in zip(*g)])]
# p=lambda g:[*zip(*[s[:-(u:=sum(s)//4)|16]+u*(8,)for s in zip(*g)])]
p=lambda g:[*zip(*map(lambda*s:s[:-(u:=sum(s)//4)|16]+u*(8,),*g))]
