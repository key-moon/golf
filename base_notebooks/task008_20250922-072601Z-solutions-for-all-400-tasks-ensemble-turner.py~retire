def p(s,u=enumerate):
 q,E=[(q,b)for(q,E)in u(s)for(b,d)in u(E)if d==2],[(q,b)for(q,E)in u(s)for(b,d)in u(E)if d==8]
 if not q or not E:return s
 k=lambda b:(min(q for(q,E)in b),max(q for(q,E)in b),min(q for(E,q)in b),max(q for(E,q)in b));l,n,a,r=k(q);e,i,w,k=k(E);b=d=0
 if r<w:d=w-r-1
 elif k<a:d=k-a+1
 elif n<e:b=e-n-1
 elif i<l:b=i-l+1
 e,n={*q},{*E};return[[8 if(q,E)in n else 2 if(q-b,E-d)in e else 0 for(E,k)in u(s[0])]for(q,E)in u(s)]