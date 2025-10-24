def p(s,u=enumerate):
 q,f=[(q,b)for(q,f)in u(s)for(b,d)in u(f)if d==2],[(q,b)for(q,f)in u(s)for(b,d)in u(f)if d==8]
 if not q or not f:return s
 m=lambda b:(min(q for(q,f)in b),max(q for(q,f)in b),min(q for(f,q)in b),max(q for(f,q)in b));l,n,a,r=m(q);e,i,w,m=m(f);b=d=0
 if r<w:d=w-r-1
 elif m<a:d=m-a+1
 elif n<e:b=e-n-1
 elif i<l:b=i-l+1
 e,n={*q},{*f};return[[8if(q,f)in n else 2if(q-b,f-d)in e else 0for(f,m)in u(s[0])]for(q,f)in u(s)]