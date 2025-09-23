# best: 118(jailctf merger) / others: 120(ox jam), 120(4atj sisyphus luke Seek mukundan), 120(xsot ovs att joking mewheni), 129(cubbus), 136(intgrah jimboko awu macaque sammyuri)
# ======================================================= 118 ========================================================
# TODO: gcdシフト再帰
# lambda g,c=-43,s=[]:g*c or p([*zip(*([r for r in g if(max(r)not in s and(s:=[*s,*r])and r.count(max(r))==1)-1]+g[:1]*9)[:len(g)])][::-1],c+1)
# 0<sum(r)==max(r)
# r.count(max(r))==1
# lambda g,c=-3,s=[]:g*c or p([*zip(*([s:=r for r in g if((max(r)in s)-1and 0<sum(r)==max(r))-1]+g[:1]*99)[len(g)-1::-1])],c+1)

# 以前の行に要素がなく、かつ長さが1のものを消すという方向
# lambda g,c=-3,s=[0]:g*c or p([*zip(*([s:=r for r in g if max(r) in s or sum(r)!=max(r)]+g[:1]*99)[len(g)-1::-1])],c+1)
# lambda g,c=-3,s=[0]:g*c or p([*zip(*([s:=r for r in g if max(r)in s or(sum(r)in r)-1]+g[:1]*99)[len(g)-1::-1])],c+1)
# lambda g,c=-3,s=[0]:g*c or p([*zip(*([s:=r for r in g if(max(r)in s)>=(sum(r)in r)]+g[:1]*99)[len(g)-1::-1])],c+1)
p=lambda g,c=-3,s=[0]:g*c or p([*zip(*[s:=r for r in g+g[:1]*99if(max(r)in s)>=(sum(r)in r)][len(g)-1::-1])],c+1)

# [s:=r for r in g if(max(r)in s)>=(sum(r)in r)]
# [*filter(lambda r:(max(r)in s)>=(sum(s:=r)in r),g)]
