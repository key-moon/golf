# best: 51(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 52(intgrah jimboko awu macaque sammyuri), 52(xsot ovs att joking mewheni), 53(jacekwl Potatoman nauti), 55(HETHAT), 55(Afordancja)
# ======================= 51 ======================
# lambda g:g*0!=0and sum([map(p,g)]*3,())or g
# lambda s:sum([[v*0!=0and p(v)or v]*3for v in s],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g)]]*3),())or g
