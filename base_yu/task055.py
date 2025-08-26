# best: 87(4atj) / others: 93(mukundan), 101(luke), 101(luke/sisyphus/Seek), 104(joking+MWI), 104(joking/MWI)
# ========================================= 87 ========================================
# p=lambda g,E=enumerate:[[s[j]or[0,2,0,4,6,3,0,1,0][(sum(s[:j])+sum(t[:i])*3)//8] for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or[0,4,0,2,6,1,0,3,0][(sum(s[:j])*3+sum(t[:i]))//8]for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or~-b""[(sum(s[:j])*3+sum(t[:i]))//8]for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,c=0:[(c:=c+all(s),d:=0)or[v or[0,4,0,2,6,1,0,3,0][c*3+(d:=d+(t>0))] for v,t in zip(s,zip(*g))]for s in g]
# p=lambda g,c=0:[(c:=c+all(s),d:=1)and[[8,0,4,0,2,6,1,0,3,0][(v<1)*(c+(d:=d+v//8*3))]for v in s]for s in g]
p=lambda g,c=0:[(c:=c+all(s),d:=1)and[b"	"[(v<1)*(c+(d:=d+v//8*3))]-1for v in s]for s in g]

# 020
# 463
# 010

