# best: 83(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 95(ox jam), 95(xsot ovs att joking mewheni), 105(JRKX), 105(jonas ryno kg583 kabutack), 105(jonas ryno kg583)
# ======================================= 83 ======================================
# p=lambda g,E=enumerate:[[s[j]or[0,2,0,4,6,3,0,1,0][(sum(s[:j])+sum(t[:i])*3)//8] for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or[0,4,0,2,6,1,0,3,0][(sum(s[:j])*3+sum(t[:i]))//8]for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or~-b""[(sum(s[:j])*3+sum(t[:i]))//8]for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,c=0:[(c:=c+all(s),d:=0)or[v or[0,4,0,2,6,1,0,3,0][c*3+(d:=d+(t>0))] for v,t in zip(s,zip(*g))]for s in g]
# p=lambda g,c=0:[(c:=c+all(s),d:=1)and[[8,0,4,0,2,6,1,0,3,0][(v<1)*(c+(d:=d+v//8*3))]for v in s]for s in g]
# p=lambda g,c=0:[(c:=c+all(s),d:=1)and[b"	"[(v<1)*(c+(d:=d+v//8*3))]-1for v in s]for s in g]
# p=lambda g,c=0:[(c:=c+all(s)*3,d:=0)and[[1602080>>c+(d:=d+v)&7,v][v>0]for v in s]for s in g]
p=lambda g,i=0:[(i:=i+r[0],j:=i)and[[586768>>(j:=j+c//8*3)&7,c][c>0]for c in r]for r in g]
# a=0
# a|=4<<3
# a|=2<<8
# a|=6<<11
# a|=1<<14
# a|=3<<19
# print(a)

# 020
# 463
# 010
