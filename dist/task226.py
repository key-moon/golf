A=sum
p=lambda g,E=enumerate:[[s[j]or A(-~k*(A(s[:j])*2==k*A(s))*(A(t[:i])*2==k*A(t))for k in(0,1,2))for(j,t)in E(zip(*g))]for(i,s)in E(g)]