# best: 50(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II) / others: 51(cubbus), 51(Code Golf International), 51(4atj sisyphus luke Seek mukundan), 51(jailctf merger), 51(biz)
# ====================== 50 ======================
# lambda g:g*0!=0and sum([map(p,g)]*3,())or g
# lambda s:sum([[v*0!=0and p(v)or v]*3for v in s],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g)]]*3),())or g
