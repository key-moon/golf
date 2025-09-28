# best: 51(cubbus, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 52(ox jam), 52(intgrah jimboko awu macaque sammyuri), 53(jacekwl Potatoman nauti), 53(jacekw Potatoman nauti natte), 53(jacekw Potatoman nauti)
# ======================= 51 ======================
# lambda g:g*0!=0and sum([map(p,g)]*3,())or g
# lambda s:sum([[v*0!=0and p(v)or v]*3for v in s],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g)]]*3),())or g
