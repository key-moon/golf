def p(g):
 val_h=len(g);val_w=len(g[0]);val_v=set()
 for val_i in range(val_h):
  for val_j in range(val_w):
   if g[val_i][val_j]!=8 and (val_i,val_j) not in val_v:
    val_st=[(val_i,val_j)];val_comp=[];val_s={}
    val_v.add((val_i,val_j))
    while val_st:
     val_ci,val_cj=val_st.pop();val_comp.append((val_ci,val_cj))
     val_x=g[val_ci][val_cj]
     if val_x>0 and val_x not in val_s:val_s[val_x]=(val_ci,val_cj)
     for val_di,val_dj in((1,0),(-1,0),(0,1),(0,-1)):
      val_ni,val_nj=val_ci+val_di,val_cj+val_dj
      if 0<=val_ni<val_h and 0<=val_nj<val_w and g[val_ni][val_nj]!=8 and (val_ni,val_nj) not in val_v:
       val_v.add((val_ni,val_nj));val_st.append((val_ni,val_nj))
    if len(val_s)==2:
     val_a,val_b=sorted(val_s);val_ia,val_ja=val_s[val_a];val_p=(val_ia+val_ja)&1
     for val_ci,val_cj in val_comp:
      g[val_ci][val_cj]=val_a if ((val_ci+val_cj)&1)==val_p else val_b
 return g
