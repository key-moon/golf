# best: 93(jailctf merger) / others: 94(ox jam), 95(biz), 97(Yuchen20), 98(4atj sisyphus luke Seek mukundan), 98(Bulmenisaurus)
# ============================================ 93 ===========================================
# p=lambda g,E=enumerate:(n:=len(g))and[[v and g[[-1,0][i+2<n//2]][[-1,0][j+2<n//2]] for j,v in E(s[2:-2])]for i,s in E(g[2:-2])]
# p=lambda g,E=enumerate:(n:=len(g)//2-2)and[[v and g[[-1,0][i<n]][[-1,0][j<n]]for j,v in E(s[2:-2])]for i,s in E(g[2:-2])]
# p=lambda g:(R:=range(n:=len(g)-4))and[[g[i+2][j+2]and g[[-1,0][i*2<n]][[-1,0][j*2<n]]for j in R]for i in R]
# p=lambda g:(R:=range(n:=len(g)-4))and[[g[i+2][j+2]and g[-(i*2>=n)][-(j*2>=n)]for j in R]for i in R]
# p=lambda g:(R:=range(2,n:=len(g)-2))and[[g[i][j]and g[-(i*2>n)][-(j*2>n)]for j in R]for i in R]
def p(g):
 R=range(2,n:=len(g)-2)
 return[[g[i][j]and g[-(i*2>n)][-(j*2>n)]for j in R]for i in R]
