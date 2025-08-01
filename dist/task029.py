def p(AE):
 for AD in set(sum(AE,[])):
  AA=[(i,j)for i,r in enumerate(AE)for j,v in enumerate(r)if v==AD];AF,AG=min(AA);AB,AC=max(AA)
  if AB-AF>1<AC-AG and all((i in(AF,AB)or j in(AG,AC))for i,j in AA):
   return[r[AG+1:AC]for r in AE[AF+1:AB]]