def p(y):
	p=y;b,O=len(p),len(p[0])
	def F(T,U):return{(p,t)for(p,v)in enumerate(T)for(t,m)in enumerate(v)if m==U}
	def d(I):p=I;v=min(p for(p,v)in p);t=min(p for(v,p)in p);return v,t
	def r(I):
		p=I
		if not p:return 0,0,-1,-1
		v=min(p for(p,v)in p);t=max(p for(p,v)in p);m=min(p for(v,p)in p);a=max(p for(v,p)in p);return v,m,t,a
	def Z(T):return tuple(tuple(p)for p in zip(*T[::-1]))
	def M(T):return tuple(tuple(p[::-1])for p in T[::-1])
	def W(T):return tuple(tuple(p[::-1])for p in zip(*T[::-1]))[::-1]
	def B(I):
		p=I
		if not p:return set()
		v,t=d(p);return{(p-v,m-t)for(p,m)in p}
	def x(I):
		p=I
		if not p:return 0,0
		v,t,m,a=r(p);return m-v+1,a-t+1
	def U(T,U,I):
		p=[list(p)for p in T]
		for(v,t)in I:
			if 0<=v<b and 0<=t<O:p[v][t]=U
		return tuple(tuple(p)for p in p)
	v=F(p,1);y=F(p,4)
	if not v:return p
	i=min(p for(p,v)in v);G=max(p for(p,v)in v);S=min(p for(v,p)in v);e=max(p for(v,p)in v);u=i,S;t=tuple(tuple(p[v][S:e+1])for v in range(i,G+1));o=[t,Z(t),M(t),W(t)]
	def i(T):return tuple(tuple(p[::-1])for p in T)
	o+=[i(p)for p in o];q=set()
	for J in o:
		m={(p,t)for(p,v)in enumerate(J)for(t,m)in enumerate(v)if m==4};f={(p,t)for(p,v)in enumerate(J)for(t,m)in enumerate(v)if m==1};E={(p+u[0],v+u[1])for(p,v)in m};G=y;S=d(m)if m else(0,0);n=d(f)if f else(0,0);j=n[0]-S[0];N=n[1]-S[1];K=B(m);H=B(f);X,k=x(K);Q=b-X+1;L=O-k+1
		if Q<0 or L<0:continue
		for a in range(Q):
			for Y in range(L):
				C={(p+a,v+Y)for(p,v)in K};w={(p,v)for(p,v)in G if a<=p<a+X and Y<=v<Y+k}
				if w==C:P={(p+a+j,v+Y+N)for(p,v)in H};q.update(P)
	z=U(p,1,q);return z