# best: 85(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 86(LogicLynx), 87(FuunAgent), 88(Team JYCDT), 88(jailctf merger), 88(HIMAGINE THE FUTURE.)
# ======================================== 85 =======================================
# p=lambda g:[sorted(set(a:=sum(g,[])),key=a.count)[1:2]*2]*2
# p=lambda g:[sorted(set(a:=sum(g,[])),key=lambda c:(x:=max(s.count(c)for s in g))*(a.count(c)-2*x+4))[1:2]*2]*2
p=lambda g:[max([[s.count(v)*t.count(v),v]for s in g for*t,v in zip(*g,s)if v])[1:]*2]*2
