# 囲まれた部分の抽出
#  for _ in 1,2:g=[*map(list,zip(*filter(lambda x:a in x,g)))]
# 112
# def p(g):
#  a=min(s:=sum(g,[]),key=s.count)
#  for _ in 1,2:g=[*map(list,zip(*[r for r in g if a in r]))]
#  return g
# 101
# def p(g):
#  a=min(s:=sum(g,[]),key=s.count)
#  return[r[r.index(a):][:s.count(a)//4+1] for r in g if a in r]
# p=lambda g:[r[i:][:s.count(a)//4+1]for r in g if(i:=[*r,(a:=min(s:=sum(g,[]),key=s.count))].index(a))>25]
# 96
# p=lambda g:[r[r.index(a):][:s.count(a)//4+1]for r in g if(a:=min(s:=sum(g,[]),key=s.count))in r]
# 95
# p=lambda g:[r[r.index(a):][:k(a)//4+1]for r in g if(a:=min(s:=sum(g,[]),key=(k:=s.count)))in r]
# ============================= best: 78 by luke =============================01234567890123456
p=lambda g:[r[r.index(a):][:k(a)//4+1]for r in g if(a:=min(s:=sum(g,[]),key=(k:=s.count)))in r]
