# best: 85(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 90(natte), 95(jacekwl Potatoman nauti), 129(JRKX), 129(jonas ryno kg583 kabutack), 129(jonas ryno kg583)
# ======================================== 85 =======================================
# p=lambda g,c=2:c and p([*zip(*[g[i]for i in range(len(g))if~-max(max(g[:i+1]))*~-max(max(g[i:]))])],c-1)or[[v>1 and v for v in s]for s in g]
# p=lambda g,c=4:c and p([*zip(*[[v>1 and v for v in g[i]]for i in range(len(g))if 1<max(max(g[i:]))][::-1])],c-1)or g
# p=lambda g,c=4:(u:=[])or c and p([*zip(*[[v>1 and v for v in s]for s in g if 1<max(u:=u+[*s])][::-1])],c-1)or g
# p=lambda g,c=4:c and p((u:=[])+[*zip(*[eval(str(s).replace(*"10"))for s in g[::-1]if 1<max(u:=u+[*s])])],c-1)or g
# p=lambda g,c=4:c and p((u:=[])+[*zip(*[[v*(v>1)for v in s]for s in g[::-1]if 1<max(u:=u+[*s])])],c-1)or g
# p=lambda g,c=4:c and p((u:=[])+[[v*(v>1)for v in s]for s in zip(*g[::-1])if 1<max(u:=u+[*s])],c-1)or g
# p=lambda g,c=4:c and p((u:=())or[[v*(v>1)for v in s]for s in zip(*g[::-1])if 1<max(u:=u+s)],c-1)or g
p=lambda g,c=-3:g*c or p((u:=())or[[v*(v>1)for v in s]for s in zip(*g[::-1])if 1<max(u:=u+s)],c+1)
