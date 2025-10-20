# best: 85(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 88(jailctf merger), 88(ox jam), 96(jacekw Potatoman nauti natte), 96(import itertools), 97(ShadowPrompt Labs)
# ======================================== 85 =======================================
# p=lambda g:[sorted(set(a:=sum(g,[])),key=a.count)[1:2]*2]*2
# p=lambda g:[sorted(set(a:=sum(g,[])),key=lambda c:(x:=max(s.count(c)for s in g))*(a.count(c)-2*x+4))[1:2]*2]*2
p=lambda g:[max([[s.count(v)*t.count(v),v]for s in g for*t,v in zip(*g,s)if v])[1:]*2]*2
