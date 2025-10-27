# best: 132(HIMAGINE THE FUTURE.) / others: 134(Code Golf International), 134(4atj sisyphus luke Seek mukundan), 135(ox jam), 136(import itertools), 136(Tony Li)
# ============================================================== 132 ===============================================================
# p=lambda g,c=15,d=8:-c*g or[(l:=0)or[l:=v and[1+(v.bit_count()==8),v|l|(v<9)*(d:=d*2)][c<15]for v in s]for s in zip(*p(g,c-1))][::-1]
p=lambda g,c=15,d=8:-c*g or[(l:=0)or[l:=v and[-59%v.bit_count()%3,v|l|(v<9)*(d:=d*2)][c<15]for v in s]for s in zip(*p(g,c-1))][::-1]
