# best: 58(jacekw Potatoman nauti natte, Code Golf International, natte, import itertools, ox jam) / others: 60(jailctf merger), 60(intgrah jimboko awu macaque sammyuri), 61(jonas ryno kg583 kabutack), 61(open source), 61(cubbus)
# ========================== 58 ==========================
p=lambda g:[[x&y for x in s for y in t]for s in g for t in g]
# p=lambda g,X=range(9):[[g[r//3][c//3]&g[r%3][c%3]for c in X]for r in X]
# p=lambda g:[sum(([[0]*3,g[i%3]][g[i//3][j]>0]for j in(0,1,2)),[])for i in range(9)]
