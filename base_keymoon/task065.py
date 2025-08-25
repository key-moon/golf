# best: 101(4atj) / others: 103(mukundan), 104(joking+MWI), 104(joking/MWI), 109(Bulmenisaurus), 109(duckyluuk)
# 転置再帰だと 3x3の判定ができない
# lambda g:(R:=(0,(a:=len(g)//2)+1))and min(p:=[[r[j:j+a]for r in g[i:i+a]]for i in R for j in R],key=p.count)
# =============================================== 101 ===============================================
p=lambda g:(a:=len(g)//2)and min(p:=[[r[j:j+a]for r in g[i:i+a]]for i in(0,a+1)for j in(0,a+1)],key=p.count)
