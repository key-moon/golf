def p(g,L=len,R=range):
 h,w,d=L(g),L(g[0]),{}
 for r in R(h):
  for c in R(w):
    C=g[r][c]
    if C in d:
     d[C]['r']+=[r]
     d[C]['c']+=[c]
    else:
     d[C]={'r':[r],'c':[c]}
 X=sorted([[L(d[k]['r'])*(max(d[k]['c'])-min(d[k]['c'])),k] for k in d if k>0])[0][1]
 g=[[X if C==X else 0 for C in R] for R in g]
 d=d[X]
 g=[R[min(d['c']):max(d['c'])+1] for R in g]
 g=g[min(d['r']):max(d['r'])+1]
 return g