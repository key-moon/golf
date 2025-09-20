# best: 109(jailctf merger) / others: 111(ox jam), 111(4atj sisyphus luke Seek mukundan), 111(xsot ovs att joking mewheni), 114(intgrah jimboko awu macaque sammyuri), 117(jacekw Potatoman nauti)
# =================================================== 109 ===================================================

# import re;p=lambda g,c=-359:c*g or[*zip(*eval(re.sub(r"0(?=, ([1-79])(.{%d})?, ([1-79]))"%(len(g)*3-1),r"\3",str(p(g,c+1))))[::1|c%3%-2])]
# import re;p=lambda g,c=-359:c*g or p(eval(re.sub("0(?=, [1-79](.{%d})?, ([1-79]))"%~-len(g*3),r"\2",str([*zip(*g[::1|c%3%-2])]))),c+1)

# p=lambda g,c=-359:c*g or[*zip(*[(l:=0)or[(v<1<=l%8and sum({*sum(g,[])})-8-l)+(l:=v)for v in s]for s in p(g,c+1)][::-1])]
# lambda g,c=-359:c*g or[(l:=0)or[(v<1<=l%8and sum({*sum(g,[])})-8-l)+(l:=v)for v in s]for s in zip(*p(g,c+1)[::-1])]
p=lambda g,c=-359:c*g or[(l:=0)or[(v<1<=l%8)*sum({*sum(g,[-8-l])})+(l:=v)for v in s]for s in zip(*p(g,c+1)[::-1])]

# def p(g):
#  u=sum({*sum(g,[])})-8
#  for _ in range(360):
# #   g=[(l:=0)or[(v or l%8 and u-l,(l:=v))[0] for v in s]for s in zip(*g[::-1])]
#   g=[(l:=0)or[(v<1<=l%8and u-l)+(l:=v)for v in s]for s in zip(*g[::-1])]
#  return g

# import re
# def p(g):
#  for c in range(360):
#   g=eval(re.sub(r"0(?=, ([1-79])(.{%d})?, ([1-79]))"%(len(g[0])*3-1),r"\3",str(g)))
#   g=[*zip(*g[::1|c%3%-2])]
#  return g
