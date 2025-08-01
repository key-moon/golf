# r=range
# def p(g):
#  h,w=len(g),len(g[0])
#  s=any(0<g[i//w][i%w]!=g[i//w+2][i%w]>0 for i in r((h-2)*w))+2
#  return[*filter(None,[[g[[i-s,i+s][i+s<h]][[j-s,j+s][j+s<w]]for j in r(w)if g[i][j]<1]for i in r(h)])]
r=range
p=lambda g:(w:=len(g),s:=any(0<g[i//w][i%w]!=g[i//w+2][i%w]>0for i in r((w-2)*w))+2)and[*filter(None,[[g[[i-s,i+s][i+s<w]][[j-s,j+s][j+s<w]]for j in r(w)if g[i][j]<1]for i in r(w)])]
