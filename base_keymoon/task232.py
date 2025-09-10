# best: 58(jailctf merger) / others: 61(4atj sisyphus luke Seek mukundan), 61(xsot ovs att joking mewheni), 61(jonas ryno kg583), 61(JRK), 70(duckyluuk)
# lambda g:[(a:=[0,0])and eval("(a:=[r.pop()or -a[1]//~a[1]*-5,a[0]])[0],"*len(r))for r in g]
# ========================== 58 ==========================
# lambda g:[([0]*[*s,1].index(v:=max(*s,1))+[v,5]*9)[:len(s)]for s in g]
# lambda g:[([0]*r.index(m:=max(r))+[m,5-0**m*5]*9)[:len(r)]for r in g]
# lambda g:[([0]*r.index(m:=max(r))+[m,m//~m*-5]*9)[:len(r)]for r in g]
# lambda g:[(i:=0)or[[i*-5,max(r)][i:=~i+0**c]for c in r]for r in g] <- failed
p=lambda g:[(i:=0)or[[0,5,max(r)][i:=-i+c//~c]for c in r]for r in g]









