# best: 59(luke, sisyphus) / others: 67(Bulmenisaurus), 67(natte), 67(biz), 68(kabutack), 69(joking)
# =========================== 59 ==========================
# p=lambda g:sum([[sum([[v/5]*3for v in s[1::3]],[])]*3for s in g[1::3]],[])
p=lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
