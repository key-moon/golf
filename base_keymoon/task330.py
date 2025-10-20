# best: 134(4atj sisyphus luke Seek mukundan, Code Golf International) / others: 135(ox jam), 136(import itertools), 140(JRKKX), 140(biz), 141(intgrah jimboko awu macaque sammyuri)
# =============================================================== 134 ================================================================
# p=lambda g,c=15,d=8:-c*g or[(l:=0)or[l:=v and[1+(v.bit_count()==8),v|l|(v<9)*(d:=d*2)][c<15]for v in s]for s in zip(*p(g,c-1))][::-1]
p=lambda g,c=15,d=8:-c*g or[(l:=0)or[l:=v and[-59%v.bit_count()%3,v|l|(v<9)*(d:=d*2)][c<15]for v in s]for s in zip(*p(g,c-1))][::-1]
