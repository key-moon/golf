def j(r):return list(zip(*r[::-1]))
def p(r,u=len,l=range):
 m=0
 if max(r[0].count(l)for l in l(10))-1<u(r[0])/2:m=1;r=j(r)
 o,p=u(r),u(r[0])
 for d in l(o):o=sorted([[r[d].count(l),l]for l in l(10)])[-1][1];r[d]=[o]*p
 if m:r=j(j(j((r))))
 return r