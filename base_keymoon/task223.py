# best: 51(jailctf merger, cubbus, 4atj sisyphus luke Seek mukundan, Code Golf International, biz) / others: 52(Tony Li), 52(ox jam), 52(intgrah jimboko awu macaque sammyuri), 52(adakoda), 52(import itertools)
# ======================= 51 ======================
# lambda g:g*0!=0and sum([map(p,g)]*3,())or g
# lambda s:sum([[v*0!=0and p(v)or v]*3for v in s],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g)]]*3),())or g
