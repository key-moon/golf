r=range
p=lambda g:(w:=len(g),s:=any(0<g[i//w][i%w]!=g[i//w+2][i%w]>0for i in r((w-2)*w))+2)and[*filter(len,[[g[[i-s,i+s][i+s<w]][[j-s,j+s][j+s<w]]for j in r(w)if g[i][j]<1]for i in r(w)])]