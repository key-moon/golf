# best: 65(jailctf merger) / others: 74(mukundan), 74(4atj sisyphus luke Seek), 106(MasukenSamba), 112(xsot ovs att joking mewheni), 112(natte)
# ============================== 65 =============================
# p=lambda g:(u:=[*zip(*g)])and[*map(list,zip(*[u[i%(8-2*(u[3:6]in(u[:3],u[2::-1])))] for i in range(15)]))]
# p=lambda g:(u:=[*zip(*g)])and[*map(list,zip(*(u[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]))]
# p=lambda g:[*map(list,zip(*((u:=[*zip(*g)])[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]))]
# p=lambda g:(u:=[*zip(*g)])and[(s[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]for s in g]
p=lambda g:[(s[:8-2*((u:=[*zip(*g)])[3:6]in(u[:3],u[2::-1]))]*3)[:15]for s in g]
