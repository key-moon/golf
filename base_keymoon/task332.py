# best: 58(luke) / others: 64(mukundan), 64(nauti), 65(4atj), 65(sisyphus), 67(kg583)
# lambda g:[(a:=[1,.6])and[c*(a:=a[::-1])[0]for c in r[::-1]][::-1]for r in g]
# lambda g:[[c*[1,.6][i+len(r)&1]for i,c in enumerate(r)]for r in g]
# lambda g:[(a:=5)and[(0<c)*(a:=a^6)for c in r[::-1]][::-1]for r in g]
# lambda g:[[(0<c)*(a:=a^6)for c in r]for r in g if(a:=3^6*len(r)%12)]
# lambda g:[(a:=.6+.8*len(r)%1.6)and[c*(a:=1.6-a)for c in r]for r in g]
# lambda g:[[v*.6**(len(s)-i&1)for i,v in enumerate(s)]for s in g]
# ========================== 58 ==========================
p=lambda g:[eval(".6**(len(r)%2)*r.pop(0),"*len(r))for r in g]
