def p(o,t=len,i=range):
 h,w=t(o),t(o[0])
 for r in i(h//2):
  if len(set(o[r]))>2:o[r+(h//2)+1]=o[r][:]
 x=o[0].count(4)+1
 for r in i(h//2,h):
  if len(set(o[r]))>2:o[r-(h//2)-1]=o[r][:]
 x=o[0].count(4)+1
 if x==1:
  for r in i(h//2):
   for j in i(w):e=max([o[r][j],o[r+(h//2)+1][j]]);o[r][j]=e;o[r+(h//2)+1][j]=e
 for r in i(h):
  for j in i(w//x):
   for c in i(x):o[r][j]=max([o[r][j],o[r][j+(w//x+1)*c]]);o[r][j+(w//x+1)*c]=max([o[r][j],o[r][j+(w//x+1)*c]])
 for r in i(h):
  for j in i(w//x):
   for c in i(x):o[r][j]=max([o[r][j],o[r][j+(w//x+1)*c]]);o[r][j+(w//x+1)*c]=max([o[r][j],o[r][j+(w//x+1)*c]])
 return o