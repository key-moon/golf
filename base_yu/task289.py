# best: 63(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, biz) / others: 64(intgrah jimboko awu macaque sammyuri), 67(lv1.dev), 72(import itertools), 74(jacekwl Potatoman nauti), 74(jacekw Potatoman nauti natte)
# ============================= 63 ============================
p=lambda g:sum([(k:=len({*str(g)})-5)*[sum(zip(*[s]*k),())]for s in g],[])
