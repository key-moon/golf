def p(g,k=0,u=[[2]*99]):
 if k<1:g=p(g,k:=str(g).count('2')//12)
 return[*zip(*u+sum([k*[s]for s in g if{*s}-{0,2}],[])+u)]