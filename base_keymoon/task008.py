# best: 84(4atj sisyphus luke Seek mukundan) / others: 89(mukundan), 94(xsot ovs att joking mewheni), 95(4atj sisyphus luke Seek), 103(jailctf merger), 103(natte)
# ======================================= 84 =======================================
# lambda g,c=-35:g*c or p([*zip(*[g.pop((1-any(g[i:=g.index(max(g,key=max))-1]))*(0<i)*i)]+g)][::-1],c+1)
# lambda g,c=-35:g*c or p([*zip(*[g.pop(any(g[i:=g.index(max(g,key=max))-1])**(0<i)*-i+i)]+g)][::-1],c+1)
# lambda g,c=-35:g*c or p([*zip(g.pop((any(g[i:=g.index(max(g,key=max))-1])*99<i)*i),*g)][::-1],c+1)
p=lambda g,c=-35:g*c or p([*zip(g.pop((max(g[i:=g.index(max(g,key=max))-1])*9<i)*i),*g)][::-1],c+1)
# lambda g,c=-35:g*c or p([*zip(g.pop(                             ),*g)][::-1],c+1)

# max([8,2,1]+g,key=max)
