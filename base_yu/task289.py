# best: 63(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, biz) / others: 72(import itertools), 74(jacekwl Potatoman nauti), 74(jacekw Potatoman nauti natte), 74(jacekw Potatoman nauti), 74(HIMAGINE THE FUTURE.)
# ============================= 63 ============================
p=lambda g:sum([(k:=len({*str(g)})-5)*[sum(zip(*[s]*k),())]for s in g],[])
