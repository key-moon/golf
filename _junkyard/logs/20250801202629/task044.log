def p(val_g):
 val_u=[x for r in val_g for x in r];val_D=[1,-1,10,-10]
 def val_f(val_c):
  val_V=[0]*100;val_C=[]
  for val_i in range(100):
   if val_u[val_i]==val_c and not val_V[val_i]:
    val_S=[val_i];val_V[val_i]=1
    for val_p in val_S:
     for val_d in val_D:
      val_q=val_p+val_d
      if 0<=val_q<100 and abs(val_p%10-val_q%10)<2 and val_u[val_q]==val_c and not val_V[val_q]:
       val_V[val_q]=1;val_S.append(val_q)
    val_C.append(val_S)
  return val_C
 val_c5=val_f(5)
 val_o=[(val_c,val_S)for val_c in set(val_u)-{0,5}for val_S in val_f(val_c)]
 for val_S in val_c5:
  val_xs=[v//10 for v in val_S];val_ys=[v%10 for v in val_S]
  val_r0,val_r1=min(val_xs),max(val_xs);val_c0,val_c1=min(val_ys),max(val_ys)
  val_H=[10*val_r+val_c for val_r in range(val_r0,val_r1+1)for val_c in range(val_c0,val_c1+1)if val_u[10*val_r+val_c]==0]
  val_h0=min(val_H);val_hs={v-val_h0 for v in val_H}
  for val_c,val_S2 in val_o:
   val_m=min(val_S2);val_ss={v-val_m for v in val_S2}
   if val_ss==val_hs:
    for v in val_H:val_u[v]=val_c
    for v in val_S2:val_u[v]=0
    break
 return [val_u[i*10:(i+1)*10]for i in range(10)]