def p(g):
 h,w=len(g),len(g[0])
 arr=[g[i][j] for i in range(h) for j in range(w)]
 arr=arr[::-1]
 res=[[0]*w for _ in range(h)]
 for idx,val in enumerate(arr):
  i,j=idx//w,idx%w;res[i][j]=val
 return res
