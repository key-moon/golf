A=max
def p(g,R=range):w=len(g);x,y,_=[i for i in R(w*w)if g[i//w][i%w]];return[[(A(abs(i-y//w),abs(j-y%w))%(y%w-x%w)==0)*A(A(g))for j in R(w)]for i in R(w)]