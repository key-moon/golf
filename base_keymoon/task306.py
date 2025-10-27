# best: 63(import itertools) / others: 71(jailctf merger), 74(HIMAGINE THE FUTURE.), 75(ox jam), 81(Code Golf International), 81(4atj sisyphus luke Seek mukundan)
# 128
# p=lambda g:[[max(g[I][J] for I in range(i%10,len(g),10) for J in range(j%10,len(r),10)) for j in range(len(r))]for i,r in enumerate(g)]
# 109
p=lambda g:[[max(c for r in g[i%10::10] for c in r[j%10::10]) for j in range(len(g[0]))]for i in range(len(g))]
# zipテクで頑張るとなんかできそうだが謎
# def p(g):
#   j=9
#   print(f"h={len(g)}, w={len(g[0])}")
#   print([[*zip(*zip(*[iter(l+[0])]*(len(l)//9)))] for l in g])
#   return[[(j:=-~j) and max(c for r in l for c in r[j%10::10]) for _ in g[0]]for l in zip(*zip(*([iter(g)]*10)))]
