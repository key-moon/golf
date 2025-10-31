# best: 118(Code Golf International) / others: 119(lv1.dev), 128(LogicLynx), 131(ox jam), 133(jailctf merger), 141(4atj sisyphus luke Seek mukundan)
# ======================================================= 118 ========================================================

# p=lambda g,z=[0]*10:[u for I in range(6400)if all(sum(u:=[[[0,*[z,*g,z][I//640+u],0][I//64%10+v]^g[I//8%8+u][I%8+v]for v in range(3)]for u in range(3)],[]))][0]
p=lambda g,z=[0]*10:max(all(sum(u:=[[([z,*g,z][I//576+u]+z)[I//64%9+v]^g[I//8%8+u][I%8+v]for v in range(3)]for u in range(3)],[]))*u for I in range(5760))
# p=lambda g,z=[0]*10:[u for I in range(80)for J in range(80)if all(sum(u:=[[[0,*[z,*g,z][I//8+u],0][J//8+v]^g[I%8+u][J%8+v]for v in range(3)]for u in range(3)],[]))][0]

# def p(g):
#  z=[0]*10
#  return [u for i in range(10)for j in range(10)for y in range(8)for x in range(8)
#          if all(sum(u:=[[[0,*[z,*g,z][i+u],0][j+v]^g[y+u][x+v]for v in range(3)]for u in range(3)],[]))][0]

# def p(g,R=(0,1,2)):
#  G=sum(g,[])
#  H=sum(zip(*g),())
#  a,b,_=sorted({*G},key=G.count)
#  y=G.index(b)//10
#  x=H.index(b)//10
#  y-=g[y+1][x:x+3]==[b]*3
#  x-=all(b==g[y+k][x+1]for k in R)
# #  x-=g[y][x+1]==g[y+1][x+1]==g[y+2][x+1]==b
#  return[[-1<y+i<10>x+j>-1 and g[y+i][x+j]or a for j in R]for i in R]

#  u=[[a]*3 for _ in range(3)]
#  for i in range(10):
#   for j in range(10):
#    if g[i][j]==b:
#     u[i-y][j-x]=b
#  return u

# def p(g):
#  G=sum(g,[])
#  a,b,_=sorted({*G},key=G.count)
#  I=[i for i in range(10)for j in range(10) if g[i][j]==b]
#  J=[j for i in range(10)for j in range(10) if g[i][j]==b]
#  y=min(I)
#  x=min(J)
#  y-=g[y+1][x:x+3]==[b]*3
#  x-=all(g[y+k][x+1]==b for k in range(3))
#  u=[[a]*3 for _ in range(3)]
#  for i,j in zip(I,J):
#   u[i-y][j-x]=b
#  return u
