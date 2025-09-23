# best: 91(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 92(ox jam), 95(JRKX), 95(kdmitrie), 95(jonas ryno kg583 kabutack), 95(jonas ryno kg583)
# =========================================== 91 ==========================================
# r=range
# def p(g):
#  h,w=len(g),len(g[0])
#  s=any(0<g[i//w][i%w]!=g[i//w+2][i%w]>0 for i in r((h-2)*w))+2
#  return[*filter(None,[[g[[i-s,i+s][i+s<h]][[j-s,j+s][j+s<w]]for j in r(w)if g[i][j]<1]for i in r(h)])]

# p=lambda g,R=range:(w:=len(g),s:=any(0<g[i//w][i%w]!=g[i//w+2][i%w]>0for i in R((w-2)*w))+2)and[*filter(len,[[g[[i-s,i+s][i+s<w]][[j-s,j+s][j+s<w]]for j in R(w)if g[i][j]<1]for i in R(w)])]
# p=lambda g:(w:=len(g),s:=(w>6)+2,R:=range(w))and[*filter(len,[[g[i+[-s,s][i<s]][j+[-s,s][j<s]]for j in R if g[i][j]<1]for i in R])]
# p=lambda g,E=enumerate:(s:=(len(g)>6)+2)and[*filter(len,[[g[i+[-s,s][i<s]][j+[-s,s][j<s]]for j,v in E(t)if v<1]for i,t in E(g)])]
# p=lambda g,E=enumerate:[*filter(len,[[g[i+[-(s:=(len(g)>6)+2),s][i<s]][j+[-s,s][j<s]]for j,v in E(t)if v<1]for i,t in E(g)])]
# p=lambda g,E=enumerate:[[g[i+[-(s:=(len(g)>6)+2),s][i<s]][j+[-s,s][j<s]]for j,v in E(t)if v<1]for i,t in E(g)if 0in t]
# p=lambda g,E=enumerate:[[t[j+[-(s:=(len(g)>6)+2),s][j<s]]for j,v in E(t)if v<1]for t in g if 0in t]
# p=lambda g,E=enumerate:[[t[j+[-(s:=(len(g)>6)+2),s][j<s]]for j,v in E(t)if v<1]for t in g if 0in t]
p=lambda g:[[t[j+[s:=(len(g)>6)+2,-s][j>=s]]for j,v in enumerate(t)if v<1]for t in g if 0in t]
