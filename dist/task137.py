A=max
def p(g,E=enumerate):w=len(g);x,y,_=[i for(i,v)in E(sum(g,[]))if v];return[[(A(abs(i-y//w),abs(j-y%w))%(y%w-x%w)==0)*A(A(g))for(j,v)in E(s)]for(i,s)in E(g)]