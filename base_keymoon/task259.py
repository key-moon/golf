# best: 85(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 86(natte), 95(jacekwl Potatoman nauti), 95(jacekw Potatoman nauti), 129(jonas ryno kg583 kabutack), 129(JRKX)
# lambda g,c=2:c and p([*zip(*[g[i]for i in range(len(g))if~-max(max(g[:i+1]))*~-max(max(g[i:]))])],c-1)or[[v>1 and v for v in s]for s in g]
# lambda g,c=4:c and p([*zip(*[[v>1 and v for v in g[i]]for i in range(len(g))if 1<max(max(g[i:]))][::-1])],c-1)or g
# lambda g,c=4:(u:=[])or c and p([*zip(*[[v>1 and v for v in s]for s in g if 1<max(u:=u+[*s])][::-1])],c-1)or g
# lambda g,c=4:c and p((u:=[])+[*zip(*[eval(str(s).replace(*"10"))for s in g[::-1]if 1<max(u:=u+[*s])])],c-1)or g
# lambda g,c=4:c and p((u:=[])+[*zip(*[[v*(v>1)for v in s]for s in g[::-1]if 1<max(u:=u+[*s])])],c-1)or g
# lambda g,c=4:c and p((u:=[])+[[v*(v>1)for v in s]for s in zip(*g[::-1])if 1<max(u:=u+[*s])],c-1)or g
# lambda g,c=4:c and p((u:=())or[[v*(v>1)for v in s]for s in zip(*g[::-1])if 1<max(u:=u+s)],c-1)or g
# lambda g,c=-3,u=():g*c or p([[v*(v>1)for v in s]for s in zip(*g[::-1])if 1<max(u:=u+s)],c+1)
# lambda g,c=-7,u=():g*c or p([[v*(v>1)for v in s]for s in zip(*g[::-1])if max(u:=u+s)],c+1)
# ======================================== 85 =======================================
p=lambda g,c=-63:g*c or p([[v*(v>1)for v in s]for s in zip(*g[any(g[-1])-2::-1])],c+1)
