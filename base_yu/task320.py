# best: 65(Code Golf International) / others: 66(LogicLynx), 66(jailctf merger), 66(HIMAGINE THE FUTURE.), 66(ox jam), 66(intgrah jimboko awu macaque sammyuri)
# ============================== 65 =============================
p=lambda g:[*zip(*[[*s][:len(s)-(u:=s.count(2)//2)]+u*[8]for s in zip(*g)])]
