# best: 51(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 52(intgrah jimboko awu macaque sammyuri), 52(xsot ovs att joking mewheni), 55(HETHAT), 56(kdmitrie), 56(mukundan)
# ======================= 51 ======================
# lambda g:g*0!=0and sum([map(p,g)]*3,())or g
# lambda s:sum([[v*0!=0and p(v)or v]*3for v in s],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g)]]*3),())or g
