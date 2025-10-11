# best: 88(import itertools) / others: 89(jailctf merger), 90(jacekw Potatoman nauti natte), 90(jacekw Potatoman nauti), 92(ox jam), 93(Yuchen20)
# ========================================= 88 =========================================
# p=lambda g:(R:=range(n:=len(g)))and[[g[i][j]or(abs(j-n//2)+i==n-2+(n-g[-2].count(0))//2)*g[-1][n//2]for j in R]for i in R]
# p=lambda g:(n:=len(g))and[[g[-(abs(j-n//2)==n-i+(g[-2].count(0)<n-1))][n//2]for j in range(n)]for i in range(2,n)]+g[-2:]
# p=lambda g:(n:=len(g))and[[g[-(abs(j-n//2)==i+2-(g[-2].count(0)>n-3))][n//2]for j in range(n)]for i in range(n-2)][::-1]+g[-2:]
# p=lambda g:(R:=range(n:=len(g)))and[[g[i][j]or g[-(abs(j-n//2)+i==n-2+(n-g[-2].count(0))//2)][n//2]for j in R]for i in R]

def p(g):
 R=range(n:=len(g))
 return[[g[i][j]or g[-(abs(j-n//2)+i==n-2+(n-g[-2].count(0))//2)][n//2]for j in R]for i in R]

# def p(g):
#  n=len(g)
#  return[[g[-(abs(j-n//2)==n-i+(g[-2].count(0)!=n-1))][n//2]for j in range(n)]for i in range(2,n)]+g[-2:]
#  return[[g[i][j]or g[-(abs(j-n//2)+i==n-2+(n-g[-2].count(0))//2)][n//2]for j in R]for i in R]
