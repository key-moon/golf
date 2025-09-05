# best: 64(att) / others: 66(luke), 71(xsot), 72(sisyphus), 74(mukundan), 80(joking)
# ============================= 64 =============================
p=lambda s:sum([[v*0!=0and p(v+s)or v]*(len({*str(s)})-5)for v in s[:3]],[])
