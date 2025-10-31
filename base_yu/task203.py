# best: 64(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, santa2024, FuunAgent, jailctf merger, HIMAGINE THE FUTURE.) / others: 66(ALE-Agent), 67(dbdr), 67(import itertools), 67(Yuchen20), 67(ox jam)
# ============================= 64 =============================
# p=lambda g:(n:=len(g)//2)and[[g[n][g[n].index(v)+n]for v in s]for s in g]
p=lambda g:[[g[n:=len(g)//2][s.index(v)+n]for v in s]for s in g]
