# best: 60(jailctf merger) / others: 61(natte), 61(duckyluuk), 61(4atj sisyphus luke Seek mukundan), 61(kdmitrie), 61(MasukenSamba)
# =========================== 60 ===========================
p=lambda g:[[x&y for x in s for y in t]for s in g for t in g]
# p=lambda g,X=range(9):[[g[r//3][c//3]&g[r%3][c%3]for c in X]for r in X]
# p=lambda g:[sum(([[0]*3,g[i%3]][g[i//3][j]>0]for j in(0,1,2)),[])for i in range(9)]
