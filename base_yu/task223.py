# best: 51(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 52(intgrah jimboko awu macaque sammyuri), 52(xsot ovs att joking mewheni), 53(jacekwl Potatoman nauti), 55(HETHAT), 55(Afordancja)
# ======================= 51 ======================
# p=lambda g:sum([[sum([[v]*3for v in s],[])]*3for s in g],[])
# p=lambda g:sum([[(s[:1]+(s*3)[1:]*3)[::3]]*3for s in g],[])

# p=lambda s,a=1:sum([[a and p(v,0)or v]*3for v in s],[])
p=lambda s:sum([[v*0!=0and p(v)or v]*3for v in s],[])


# p=lambda g:[(s[:1]+(s*3)[1:]*3)[::3]for s in(g[:1]+(g*3)[1:]*3)[::3]]
# p=lambda g:sum([[((s*3)[:8]*3+s[2:])[::3]]*3for s in g],[])

# p=lambda g:[sum([[v]*3for v in g[i//3]],[])for i in range(9)]
