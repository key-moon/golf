# best: 66(HIMAGINE THE FUTURE.) / others: 68(Code Golf International), 68(4atj sisyphus luke Seek mukundan), 68(import itertools), 68(jailctf merger), 69(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# 多分70までは縮むはず
# lambda g:[*zip(*[[s,s[:-(s.count(2)//2)]+99*(8,)][any(s)]for s in zip(*g)])] <- zipのclipを利用しようとした残骸
# lambda g:[*zip(*[s[:len(s)-(u:=s.count(2)//2)]+u*(8,)for s in zip(*g)])]
# ============================== 66 ==============================
# lambda g:[*zip(*[s[:-(u:=s.count(2)//2)or 99]+u*(8,)for s in zip(*g)])]
# lambda g:[*zip(*[s[:-(u:=sum(s)//4)or 99]+u*(8,)for s in zip(*g)])]
# p=lambda g:[*zip(*[s[:-(u:=sum(s)//4)|16]+u*(8,)for s in zip(*g)])]
p=lambda g:[*zip(*map(lambda*s:s[:-(u:=sum(s)//4)|16]+u*(8,),*g))]
