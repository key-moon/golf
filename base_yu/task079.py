# best: 123(duckyluuk, 4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni) / others: 126(jailctf merger), 129(jacekwl Potatoman nauti), 149(natte), 163(MasukenSamba), 215(cg)
# ========================================================== 123 ==========================================================
# p=lambda g,R=range(12):max(f:=[[s[j:j+3]for s in g[i:i+3]]for i in R for j in R],key=lambda x:(all(map(any,x)),f.count(x),sum(sum(x,[]))))
# p=lambda g:max(f:=[[s[i//12:][:3]for s in g[i%12:][:3]]for i in range(144)],key=lambda x:(all(map(any,x)),f.count(x),sum(sum(x,[]))))
# lambda g:max(f:=[[s[i//12:][:3]for s in g[i%12:][:3]]for i in range(144)],key=lambda x:(*map(any,x),f.count(x),sum(sum(x,[]))))
# lambda g:max(f:=[[s[i//12:][:3]for s in g[i%12:][:3]]for i in range(144)],key=lambda x:(*map(any,x+[*zip(*x)]),f.count(x)))
# lambda g:max(f:=[[s[i//12:][:3]for s in g[i%12:][:3]]for i in range(144)],key=lambda x:(*map(any,x+[*zip(*x)]),f.count(x)))
p=lambda g:max(f:=[x for i in range(144)if all(map(any,(x:=[s[i//12:][:3]for s in g[i%12:][:3]])+[*zip(*x)]))],key=f.count)

# def p(g,R=range(12)):
#  f=[[s[j:j+3]for s in g[i:i+3]]for i in R for j in R]
#  return max(f,key=lambda x:(all(map(any,x)),f.count(x),sum(sum(x,[]))))




