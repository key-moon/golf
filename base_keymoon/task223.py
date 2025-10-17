# best: 51(cubbus, 4atj sisyphus luke Seek mukundan, jailctf merger, biz) / others: 52(import itertools), 52(Tony Li), 52(adakoda), 52(ox jam), 52(intgrah jimboko awu macaque sammyuri)
# ======================= 51 ======================
# lambda g:g*0!=0and sum([map(p,g)]*3,())or g
# lambda s:sum([[v*0!=0and p(v)or v]*3for v in s],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g)]]*3),())or g
