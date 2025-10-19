# best: 57(jailctf merger) / others: 58(import itertools), 59(natte), 59(jacekw Potatoman nauti natte), 60(intgrah jimboko awu macaque sammyuri), 62(cubbus)
# ========================== 57 =========================
# ==================== best 64 by luke, att ====================
# p=lambda g:[g[0][:1]*(len(g[0])-g[0].count(g[0][0])+1)]*(len(g)-g.count(g[0])+1)
p=lambda g:[(len(s:=g[0])-s.count(s[0])+1)*s[:1]]*(len(g)-g.count(s)+1)
# p=lambda g:[(s:=g[0])[:1]*-~s.count(sum({*s})-s[0])]*(len(g)-g.count(s)+1)
# p=lambda g:[(s:=g[0])[:1]*-~s.count(*({*s}-{s[0]}))]*(len(g)-g.count(s)+1)

# def p(g):
#  w=len(g[0])-g[0].count(g[0][0])+1
#  h=len(g)-[*zip(*g)][0].count(g[0][0])+1
#  return[[g[0][0]]*w for _ in range(h)]
