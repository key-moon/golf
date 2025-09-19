# best: 60(jailctf merger) / others: 61(ox jam), 61(4atj sisyphus luke Seek mukundan), 61(HETHAT), 61(jacekwl Potatoman nauti), 61(xsot ovs att joking mewheni)
# =========================== 60 ===========================
# lambda g:[*zip(*[sorted(r,key=lambda x:x-1&3)for r in zip(*g)])]
# lambda g:[*zip(*[sorted(r,key=(1,2,0).index)for r in zip(*g)])]
# p=lambda g:[*zip(*[sorted(r,key=b"\0".find)for r in zip(*g)])]
p=lambda g:[*zip(*map(lambda*r:sorted(r,key=b"\0".find),*g))]
