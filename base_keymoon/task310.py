# best: 78(4atj sisyphus luke Seek mukundan) / others: 79(jailctf merger), 81(2F), 81(biz), 81(intgrah jimboko awu macaque sammyuri), 81(xsot ovs att joking mewheni)
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
# lambda g:[r[i:][:s.count(a)//4+1]for r in g if(i:=[*r,(a:=min(s:=sum(g,[]),key=s.count))].index(a))>25]
# 96
# lambda g:[r[r.index(a):][:s.count(a)//4+1]for r in g if(a:=min(s:=sum(g,[]),key=s.count))in r]
# 95
# lambda g:[r[r.index(a):][:k(a)//4+1]for r in g if(a:=min(s:=sum(g,[]),key=(k:=s.count)))in r]
# lambda g:[r[r.index(a):][:k(a)//4+1]for r in g if(a:=min(s:=sum(g,[]),key=(k:=s.count)))in r]
# ==================================== 78 ====================================
p=lambda g:[r[r.index(a):][:k(a)//4+1]for r in g if(a:=min(s:=sum(g,[]),key=(k:=s.count)))in r]









