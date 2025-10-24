def r(l,i,d,n):
 if not(0<=i<len(l)and 0<=d<len(l[0])):return
 if l[i][d]:return
 l[i][d]=n
 for(u,t)in[(0,-1),(0,1),(-1,0),(1,0)]:r(l,i+u,d+t,n)
def p(l):
 i,u=len(l),len(l[0]);r(l,0,0,1)
 for t in range(4):r(l,i//2-1+t%2,u//2-1+t//2,2)
 r(l,i-1,u-1,3);return l