# best: 134(4atj sisyphus luke Seek mukundan) / others: 135(ox jam), 135(xsot ovs att joking mewheni), 145(jailctf merger), 198(intgrah jimboko awu macaque sammyuri), 203(kdmitrie)
# =============================================================== 134 ================================================================
# p=lambda g,c=15,d=8:-c*g or[(l:=0)or[l:=v and[1+(v.bit_count()==8),v|l|(v<9)*(d:=d*2)][c<15]for v in s]for s in zip(*p(g,c-1))][::-1]
p=lambda g,c=15,d=8:-c*g or[(l:=0)or[l:=v and[-59%v.bit_count()%3,v|l|(v<9)*(d:=d*2)][c<15]for v in s]for s in zip(*p(g,c-1))][::-1]
