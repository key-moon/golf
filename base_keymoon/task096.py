# best: 325(xsot ovs att joking mewheni) / others: 396(jailctf merger), 442(dbdr), 449(jacekwl Potatoman), 449(jacekwl), 503(JRK)
# 罠: 中央のドットは背景と同じ色のことがある
# 矩形の辺が交わってることがある 内包してることもある
# ひどいケース(120):
#+---------
#|
#|      ..  
#|      .   
#|+==  ++   
#|  =   +   
#|   -      
#|**=   *** 
#| ==     * 
#|      + * 
#|+    ++   
#|      .   
#|      ..  
#+---------
# import re
# def p(g):
#   t=str(g)
#   # 中心かそれ以外か
#   c=min(t,key=t.count)
#   t=str([*g,*zip(*g)]);t=re.sub("[([ ,]","",t+t[::-1])
#   b=max(t,key=t.count)
#   # 中心は同じ色のケースがある
#   c=[b,c][t.count(c)<6]
#   if __debug__: SEQS = [ANSWER[i][i] for i in range(len(ANSWER)//2+1)]
#   # assert str(SEQS[-1]) == c, f"{(CASE, SEQS, c, b)=}"
#   # 反転して足してるのは * ++** + 片側からかしかマッチできないケースがあるから
#   # 360度全部試すのと同じ
#   # これなんとかしたいよね、uniqueパートがのrange based forが無駄になってる
#   # ?!の!がzlib golf的に最悪なんだけど、まあ正直縮めんの無理だよなここ
#   # backup: s={*"])",c,b};n=[v for v in sorted([z+b*len(y)+z for x,y,z in re.findall(rf"([^{b}])((?:(?!\1|\]|\)).)+?)(\1\1+)",t)],key=len)[::-1] if s^(s:=s|{v[0]})]+[({*t}-s).pop()*3,c]
#   s={*"])",c,b};n=[v for v in sorted([z+b*len(y)+z for x,y,z in re.findall(rf"([^{b}])((?:(?!\1|\]|\)).)+?)(\1\1+)",t)],key=len)[::-1] if s^(s:=s|{v[0]})]+[({*t}-s).pop()*3,c]
#   # assert len(SEQS) == len(n), f"{(a, l, SEQS, c, b)=}"
#   # assert all(str(col) == row[0] for col, row in zip(SEQS, n)), f"{(CASE, n, SEQS, c, b)=}"
#   r,l=[],[]
#   # ['448888844', '9998999', '55855', '222', '1'] -> [4, 9, 5, 2, 1]
#   for s in n:
#     u="".join(map(list.pop,l))
#     r+=[[*map(int,u+s+u[::-1])]]
#     l+=[[*s[:0:-1]]]
#   return r+r[-2::-1]

# [13,17,4,x,x,x,x],[18,18,8,x,x,x,x],[18,18,3,x,x,x,x,x,x],[19,19,1,x,x,x,x,x,x]
# w,h,b=13+R(5),13+R(5),1+R(9);c=random.sample([c for c in range(1,10)if b!=c],a:=4+R(3));l=[min(i+1,2)+R(i+(i<2))for i in range(a)]

# width, height = common.randint(13, 19), common.randint(13, 19)
# b = common.random_color()
# colors = common.random_colors(common.randint(4, 6), exclude=[b])
# lengths = []
# for i in range(len(colors)):
#   min_length, max_length = min(i + 1, 2), i + (0 if i > 1 else 1)
#   lengths.append(common.randint(min_length, max_length))
# optimal: 353

# best: 325(xsot ovs att joking mewheni) / others: 396(jailctf merger), 442(dbdr), 449(jacekwl Potatoman), 449(jacekwl), 503(J&R)

# width, height = common.randint(13, 19), common.randint(13, 19)
# b = common.random_color()
# colors = common.random_colors(common.randint(4, 6), exclude=[b])
# lengths = []
# for i in range(len(colors)):
#   min_length, max_length = min(i + 1, 2), i + (0 if i > 1 else 1)
#   lengths.append(common.randint(min_length, max_length))

# [c for c in range(1,10)if b!=c]
# filter(lambda c:c!=b,range(1,10))

# from random import *;R=randrange;
# def p(g,s=-4):
#  if s<0:h,w,b,l,*c=[[13,17,4,[1,2,2,2],4,3,1,6],[18,18,8,[1,2,2,3],0,4,2,1],[18,18,3,[1,2,2,3,3,2],6,7,8,2,1,4],[19,19,1,[1,2,2,2,3,5],1,8,3,6,2,4]][s]
#  else:seed(s+2025);w,h,b=13+R(7),13+R(7),1+R(9);c=sample([*{*range(1,10)}-{b}],a:=4+R(3));l=[1+(0<i)+R(max(1,i-1))for i in range(a)]
#  if any([h!=len(g),w!=len(g[0]),{*sum(g,[])}!={*c,b},b not in g[2]]):return p(g,s+1)
#  d=2*len(c)-1
#  o = [[b]*d for _ in "a"*d]
#  for i,(C,L) in enumerate(zip(c,l)):
#    for r, c in [(-i, -i), (-i, i), (i, -i), (i, i)]:
#      deltas = []
#      for i in range(L):
#        deltas += [(r, c + (i if c < 0 else -i))]
#        deltas += [(r + (i if r < 0 else -i), c)]
#      for dr, dc in deltas:
#        o[len(l)-1+dr][len(l)-1+dc]=C
#  return o

# ↓書きかけ
#  r=[];a=[]
#  for C,L in zip(c,l):
#   t=[*map(list.pop,a)]
#   a+=[[[C]*~-L]]
#   r+=[[t+[C]*L+t[::-1]]]
#  return r+r[:-1][::-1]

# seed bluteforcer 探索済み: 17563428
# from tqdm import tqdm;
# from itertools import count
# TARGET = {(13,17,4,1,2,2,2,4,3,1,6),(18,18,8,1,2,2,3,0,4,2,1),(18,18,3,1,2,2,3,3,2,6,7,8,2,1,4),(19,19,1,1,2,2,2,3,5,1,8,3,6,2,4)}
# for s in tqdm(count()):
#  seed(s);w,h,b=13+R(7),13+R(7),1+R(9);c=sample([*{*range(1,10)}-{b}],a:=4+R(3));l=[1+(0<i)+R(max(1,i-1))for i in range(a)]
#  generated = (h,w,b,*l,*c)
#  if generated in TARGET:
#   print(s, generated, flush=True)




# == begin zlib golf ==
import re
def p(l):
 t=str(l)
 c=min(t,key=t.count)
 t=str(l+[*zip(*l)])
 t=re.sub('[[(, ]','',t+t[::-1])
 b=max(t,key=t.count)
 c=[b,c][t.count(c)<9]
 s={*'])',b,c}
 r=[]
 l=[]
 for s in [r for r in sorted([l+b*len(p)+l for t,p,l in re.findall(rf'([^{b}])((?:(?!\)|]|\1).)+?)(\1\1+)',t)],key=len)[::-1]if s^(s:=s|{r[0]})]+[({*t}-s).pop()*3,c]:
  t=''.join(map(list.pop,l))
  l+=[[*s[:-1]]]
  r+=[[*map(int,t+s+t[::-1])]]
 return r+r[:-1][::-1]
