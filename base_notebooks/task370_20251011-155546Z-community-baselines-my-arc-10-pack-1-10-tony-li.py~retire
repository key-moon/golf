def p(g):
 R,C=len(g),len(g[0]);B=[(r,c)for r,rw in enumerate(g)for c,v in enumerate(rw)if v==0]
 if not B:return g
 cnt={};[cnt.update({v:cnt.get(v,0)+1})for v in sum(g,[])];del cnt[0];bg=max(cnt,key=cnt.get);sc_val=[k for k in cnt if k!=bg][0]
 S=[(r,c)for r,rw in enumerate(g)for c,v in enumerate(rw)if v==sc_val];rs,cs=zip(*B);m_r,M_r,m_c,M_c=min(rs),max(rs),min(cs),max(cs)
 h,w=M_r-m_r+1,M_c-m_c+1;sh=[(r-m_r,c-m_c)for r,c in B];s_rs,s_cs=zip(*S)
 dr=1 if sum(s_rs)/len(S)>=sum(rs)/len(B)else-1;dc=1 if sum(s_cs)/len(S)>=sum(cs)/len(B)else-1
 sr,sc=(dr*h,dc*w)if(m_r,m_c)in B else(dr*(h-1),dc*(w-1))
 if not sr and not sc:sr,sc=dr,dc
 elif not sr:sr=dr if h==1 else 0
 elif not sc:sc=dc if w==1 else 0
 n=[r[:]for r in g];cp=(m_r,m_c)
 while 1:
  np=(cp[0]+sr,cp[1]+sc);d=0
  for rr,rc in sh:
   pr,pc=np[0]+rr,np[1]+rc
   if 0<=pr<R and 0<=pc<C and n[pr][pc]==bg:n[pr][pc]=sc_val;d+=1
  if not d:break
  cp=np
 return n