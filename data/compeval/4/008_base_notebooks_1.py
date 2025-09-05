def p(g):
 a,b=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==2],[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==8]
 if not a or not b:return g
 f=lambda s:(min(i for i,_ in s),max(i for i,_ in s),min(j for _,j in s),max(j for _,j in s))
 mi2,ma2,mj2,maj2=f(a);mi8,ma8,mj8,maj8=f(b);dr=dc=0
 if maj2<mj8:dc=mj8-maj2-1
 elif maj8<mj2:dc=maj8-mj2+1
 elif ma2<mi8:dr=mi8-ma2-1
 elif ma8<mi2:dr=ma8-mi2+1
 s2,s8=set(a),set(b)
 return [[8 if (i,j)in s8 else 2 if(i-dr,j-dc)in s2 else 0 for j in range(len(g[0]))]for i in range(len(g))]
