# best: 101(4atj, 4atj sisyphus luke Seek) / others: 103(mukundan), 104(joking MeWhenI), 109(Bulmenisaurus), 109(duckyluuk), 114(Seek64)
# =============================================== 101 ===============================================
# 転置再帰だと 3x3の判定ができない
# lambda g:(R:=(0,(a:=len(g)//2)+1))and min(p:=[[r[j:j+a]for r in g[i:i+a]]for i in R for j in R],key=p.count)
# setによる包含判定でも3x3の判定が無理
# lambda g:(a:=(0,len(g)//2+1))and max([[(*r[j:j+a[1]],)for r in g[i:i+a[1]]]for i in a for j in a],key=set)
# lambda g:(a:=len(g)//2)and max([[(*r[j:j+a],)for r in g[i:i+a]]for i in(0,a+1)for j in(0,a+1)],key=set)

# lambda g:(a:=(0,len(g)//2+1))and max(p:=[[(*r[j:j+a[1]],)for r in g[i:i+a[1]]]for i in a for j in a],key=p.count)
# =============================================== 101 ===============================================
# lambda g:(a:=len(g)//2+1)and min(p:=[[r[j:][:2]for r in g[i:][:2]]for i in(0,a)for j in(0,a)],key=p.count)
p=lambda g:(a:=len(g)//2)and min(p:=[[r[j:j+a]for r in g[i:i+a]]for i in(0,a+1)for j in(0,a+1)],key=p.count)
