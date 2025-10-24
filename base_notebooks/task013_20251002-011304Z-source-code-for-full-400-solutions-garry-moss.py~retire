def p(n):
 u=i=q=g=l=0;m=[]
 if(u:=sum(n[0])or sum(n[-1])):n=[*zip(*n[::-1])]
 f=len(n[0])
 for p in range(len(n)):
  if n[p][0]+n[p][-1]and q<2:n[p]=[n[p][0]+n[p][-1]]*f;q+=1;m+=n[p][:1];l=p
  i+=0<q<2
 for p in range(l+i,len(n),i):n[p]=[m[g]]*f;g^=1
 if u:n=[*map(list,zip(*n))][::-1]
 return n