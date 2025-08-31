# best: 123(xsot ovs att joking mewheni, duckyluuk) / others: 129(mukundan), 129(4atj sisyphus luke Seek), 138(jailctf merger), 149(natte), 201(MasukenSamba)
# ========================================================== 123 ==========================================================
# p=lambda g,R=range(12):max(f:=[[s[j:j+3]for s in g[i:i+3]]for i in R for j in R],key=lambda x:(all(map(any,x)),f.count(x),sum(sum(x,[]))))
# p=lambda g:max(f:=[[s[i//12:][:3]for s in g[i%12:][:3]]for i in range(144)],key=lambda x:(all(map(any,x)),f.count(x),sum(sum(x,[]))))
p=lambda g:max(f:=[[s[i//12:][:3]for s in g[i%12:][:3]]for i in range(144)],key=lambda x:(*map(any,x),f.count(x),sum(sum(x,[]))))

# def p(g,R=range(12)):
#  f=[[s[j:j+3]for s in g[i:i+3]]for i in R for j in R]
#  return max(f,key=lambda x:(all(map(any,x)),f.count(x),sum(sum(x,[]))))



