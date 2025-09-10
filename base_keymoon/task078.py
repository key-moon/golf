# best: 60(jailctf merger) / others: 61(4atj sisyphus luke Seek mukundan), 61(HETHAT), 61(jacekwl Potatoman nauti), 61(xsot ovs att joking mewheni), 65(duckyluuk)
# =========================== 60 ===========================

# p=lambda g:[*map(list,zip(*[[*r[:(a:=r.index(0))]]+sorted(r[a:])[::-1]for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[[1]*(c:=r.count)(1)+[2]*c(2)+[0]*c(0)for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:"201"[x])for r in zip(*g)]))]
# p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:(x-1)%3)for r in zip(*g)]))]
# ===============================================================12345678901
p=lambda g:[*map(list,zip(*[sorted(r,key=lambda x:x-1&3)for r in zip(*g)]))]







