# best: 61(kg583, luke/sisyphus/Seek, luke) / others: 64(joking+MWI), 64(joking/MWI), 64(joking), 66(4atj), 67(att)
# lambda g:[(a:=[0,0])and eval("(a:=[r.pop()or -a[1]//~a[1]*-5,a[0]])[0],"*len(r))for r in g]
# ============================ 61 ===========================
# lambda g:[([0]*[*s,1].index(v:=max(*s,1))+[v,5]*9)[:len(s)]for s in g]
# lambda g:[([0]*r.index(m:=max(r))+[m,5-0**m*5]*9)[:len(r)]for r in g]
# lambda g:[([0]*r.index(m:=max(r))+[m,m//~m*-5]*9)[:len(r)]for r in g]
# lambda g:[(i:=0)or[[i*-5,max(r)][i:=~i+0**c]for c in r]for r in g] <- failed
p=lambda g:[(i:=0)or[[0,5,max(r)][i:=-i+c//~c]for c in r]for r in g]
