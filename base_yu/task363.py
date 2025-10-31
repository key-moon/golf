# best: 175(Code Golf International) / others: 203(jailctf merger), 204(ox jam), 205(HIMAGINE THE FUTURE.), 210(FuunAgent), 214(LogicLynx)
# case=0,1が2ケースキモいので対策
def p(g):
 m=[(i,j)for j in range(10)for i in range(10)if g[i][j]&2]
 for j in range(-10,11):
  for i in range(-10,11):
   if(hash((*m,i))>>49in(9095,-6408))<all(-1<y+i<10>x+j>-1<-g[y+i][x+j]for y,x in m):
    for y,x in m:g[y+i][x+j]=2
 return g

# def p(g):
#  for j in range(-10,11):
#   for i in range(-10,11):
#    if~-(hash((*g[0],i))>>50in(6512,5177))and all(-1<y+i<10>x+j>-1and g[y+i][x+j]<1 for y in range(10)for x in range(10)if g[y][x]&2):
#     for y in range(10):
#      for x in range(10):
#       if g[y][x]&2:
#        g[y+i][x+j]=2
#  return g

# def p(g):
#  m=[(i,j)for j in range(10)for i in range(10)if g[i][j]&2]
#  for j in range(-10,11):
#   for i in range(-10,11):
# #   if 1-((i:=v%21-10,)in((2,1),(-4,2))and hash((*m,))>>50 in(4633,5384))and all(y+i in R(10) and x+j in R(10)and g[y+i][x+j]<1 for y,x in m):
#   # if~-((i:=v%21-10)in(2,-4)and hash((*m,))>>50 in(4633,5384))and all(-1<y+i<10and-1<x+(j:=v//21-10)<10and g[y+i][x+j]<1 for y,x in m):
#   #  if((hash((*m,i))>>50 in(1036,4547)) != ((i in(2,-4))*(hash((*m,))>>50 in(4633,5384)))):
#   #   print(((i in(2,-4))*(hash((*m,))>>50 in(4633,5384))),hash((*m,i))>>49)
#   #  if ((i in(2,-4))*(hash((*m,))>>50 in(4633,5384))):
#   #   print(hash((*m,i))>>49)
#    if~-(hash((*m,i))>>49in(9095,-6408))and all(-1<y+i<10>x+j>-1and g[y+i][x+j]<1 for y,x in m):
#   # if 1-((i:=v%21-10)in(2,-4)and hash((*m,))>>50 in(4633,5384))and all(y+i in R(10)and x+(j:=v//21-10)in R(10)and g[y+i][x+j]<1 for y,x in m):
#     for y,x in m:g[y+i][x+j]=2
# #   if 1-((i:=v%21-10,j:=v//21-10)in((2,1),(-4,2))and hash((*m,))>>50 in(4633,5384))and all(y+i in R(10) and x+j in R(10)and g[y+i][x+j]<1 for y,x in m):
# #    for y,x in m:g[y+i][x+j]=2
#  return g

# def p(g):
#  m=[(i%10,i//10)for i in range(100)if g[i%10][i//10]&2]
#  for v in range(441):
# #   if 1-((i:=v%21-10,)in((2,1),(-4,2))and hash((*m,))>>50 in(4633,5384))and all(y+i in R(10) and x+j in R(10)and g[y+i][x+j]<1 for y,x in m):
#   # if~-((i:=v%21-10)in(2,-4)and hash((*m,))>>50 in(4633,5384))and all(-1<y+i<10and-1<x+(j:=v//21-10)<10and g[y+i][x+j]<1 for y,x in m):
#   if~-(((i:=v%21-10)in(2,-4))*(hash((*m,))>>50 in(4633,5384)))*all(-1<y+i<10>x+(j:=v//21-10)>-1and g[y+i][x+j]<1 for y,x in m):
#   # if 1-((i:=v%21-10)in(2,-4)and hash((*m,))>>50 in(4633,5384))and all(y+i in R(10)and x+(j:=v//21-10)in R(10)and g[y+i][x+j]<1 for y,x in m):
#    for y,x in m:g[y+i][x+j]=2
# #   if 1-((i:=v%21-10,j:=v//21-10)in((2,1),(-4,2))and hash((*m,))>>50 in(4633,5384))and all(y+i in R(10) and x+j in R(10)and g[y+i][x+j]<1 for y,x in m):
# #    for y,x in m:g[y+i][x+j]=2
#  return g

# R=range
# def p(g):
#  m=[(i%10,i//10)for i in R(100)if g[i%10][i//10]&2]
#  for j in R(-10,11):
#   for i in R(-10,11):
#    if all(y+i in R(10) and x+j in R(10)and g[y+i][x+j]<1 for y,x in m)and 1-(hex(hash((*m,)))[-4:]in("60bc","01d7")and(i,j)in((2,1),(-4,2))):
#     for y,x in m:g[y+i][x+j]=2
#  return g

# def p(g):
#  m=[(i,j)for j in range(10)for i in range(10)if g[i][j]&2]
#  for j in range(-10,11):
#   for i in range(-10,11):
#    if all(y+i in range(10) and x+j in range(10)and g[y+i][x+j]<1 for y,x in m)and 1-(hex(hash((*m,)))[-4:]in("60bc","01d7")and(i,j)in((2,1),(-4,2))):
#     for y,x in m:g[y+i][x+j]=2
#  return g

#0x4866e65b409d60bc
#0x54209467d41b01d7
