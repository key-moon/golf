# best: 63(ox jam, 4atj sisyphus luke Seek mukundan) / others: 64(jailctf merger), 64(xsot ovs att joking mewheni), 71(intgrah jimboko awu macaque sammyuri), 74(jacekwl Potatoman nauti), 83(JRKX)
# ============================= 63 ============================
p=lambda s:sum([[v*0!=0and p(v+s)or v]*(len({*str(s)})-5)for v in s[:3]],[])
