# best: 64(xsot ovs att joking mewheni) / others: 65(4atj sisyphus luke Seek mukundan), 65(jailctf merger), 66(natte), 74(Yuchen20), 75(HETHAT)
# lambda g:(k:=                      )and[s[::-k]for s in g[::k]]
# lambda g:(k:=1+g[0].index([s[0]for s in g if {*s}=={s[0]}][0]))and[s[::-k]for s in g[::k]]
# lambda g:(k:=[i+1for i,v in enumerate(g[0])if v!=g[0][0]][0])and[s[::-k]for s in g[::k]]
# lambda g:(k:=[i+1for i,s in enumerate(g)if{*s}=={s[0]}][0])and[s[::-k]for s in g[::k]]
# lambda g:[[y for x,y in zip([10]+t,t)if x!=y][::-2]for s,t in zip([0]+g,g)if s!=t][::2]
# lambda g:(k:=[i+1for i in range(8)if g[0]!=g[i]][0])and[s[::-k]for s in g[::k]]
# lambda g:[[s[::-k]for s in g[::k]]for k in range(1,8)if g[0]!=g[k-1]][0]
# lambda g:[[s[::-k]for s in g[::k]]for k in(3,4,5,6)if g[0]!=g[k-1]][0]
# lambda g:[[s[::-k]for s in g[::k]]for k in b""if g[0]!=g[k-1]][0]
# ============================= 64 =============================
# lambda g:(k:=1+g.index(min(g,key=set)))and[s[::-k]for s in g[::k]]
# f p(g):k=1+g.index(min(g,key=set));return[s[::-k]for s in g[::k]]
# lambda g:[r*0!=0and p(r)[::-1]or r for r in g if g!=(g:=r)][::2]
p=lambda g,c=2:g*0!=0and[p(g:=r,-2)for r in g if g!=r][::c]or g









