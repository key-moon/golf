# best: 128(HIMAGINE THE FUTURE.) / others: 129(Code Golf International), 129(4atj sisyphus luke Seek mukundan), 133(import itertools), 134(ox jam), 138(jailctf merger)
# ============================================================ 128 =============================================================
# lambda g,c=2**26:-c*[[-v.bit_count()%7for v in s]for s in g]or p([(l:=0)or[l:=v and v|l|(v<9)*(c:=c//2)for v in s]for s in zip(*g)][::-1],min(c-1,6))
# lambda g,c=7,d=8**40:-c*[[-v.bit_count()%7for v in s]for s in g]or p([(l:=0)or[l:=(v|l|(v<9)*(d:=d//2))&-(0<v)for v in s]for s in zip(*g)][::-1],c-1)
# lambda g,c=7,d=8**9:-c*[[-v.bit_count()%7for v in s]for s in g]or p([(l:=0)or[l:=v and v|l|(v<9)*(d:=d//2)for v in s]for s in zip(*g)][::-1],c-1)
# p=lambda g,c=11,d=8:-c*g or[(l:=0)or[l:=v and[-v.bit_count()%7,v|l|(v<9)*(d:=d*2)][c<11]for v in s]for s in zip(*p(g,c-1))][::-1]
p=lambda g,c=11,d=8:-c*g or[(l:=0)or[l:=v and[7-v.bit_count(),v|l|8//v*(d:=d*2)][c<11]for v in s]for s in zip(*p(g,c-1))][::-1]

# mapping = { 0: 0, 2: 3, 3: 2, 4: 1 } -a%5
# mapping = { 0: 0, 4: 3, 5: 2, 6: 1 } -a%7

# (v|l|(v<9)*(d:=d//2))*v%2
# v and v|l|(v<9)*(d:=d//2)

# v.bit_count()
# bin(v).count("1")
# 
