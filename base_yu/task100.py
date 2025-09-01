# best: 88(xsot ovs att joking mewheni, 4atj sisyphus luke Seek, jailctf merger) / others: 90(mukundan), 100(nauti), 105(jacekw), 105(jacekwl), 109(Bulmenisaurus)
# ========================================= 88 =========================================
# p=lambda g:[sorted(set(a:=sum(g,[])),key=a.count)[1:2]*2]*2
# p=lambda g:[sorted(set(a:=sum(g,[])),key=lambda c:(x:=max(s.count(c)for s in g))*(a.count(c)-2*x+4))[1:2]*2]*2
p=lambda g:[max([[s.count(v)*t.count(v),v]for s in g for*t,v in zip(*g,s)if v])[1:]*2]*2
