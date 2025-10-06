# best: 284(ox jam) / others: 311(jacekw Potatoman nauti natte), 312(blob2822), 325(intgrah jimboko awu macaque sammyuri), 344(jailctf merger), 362(JRKKX)
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

# best: 284(ox jam) / others: 311(jacekw Potatoman nauti natte), 312(blob2822), 325(intgrah jimboko awu macaque sammyuri), 344(jailctf merger), 362(JRKKX)

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
# # == !begin zlib golf ==
# import re
# def p(l):
#  t=str(l)
#  c=min(t,key=t.count)
#  t=str(l+[*zip(*l)])
#  t=re.sub('[[(, ]','',t+t[::-1])
#  b=max(t,key=t.count)
#  c=[b,c][t.count(c)<9]
#  s={*'])',b,c}
#  r=[]
#  l=[]
#  for s in [r for r in sorted([l+b*len(p)+l for t,p,l in re.findall(rf'([^{b}])((?:(?!\)|]|\1).)+?)(\1\1+)',t)],key=len)[::-1]if s^(s:=s|{r[0]})]+[({*t}-s).pop()*3,c]:
#   t=''.join(map(list.pop,l))
#   l+=[[*s[:-1]]]
#   r+=[[*map(int,t+s+t[::-1])]]
#  return r+r[:-1][::-1]

# width, height = common.randint(13, 19), common.randint(13, 19)
# b = common.random_color()
# colors = common.random_colors(common.randint(4, 6), exclude=[b])
# lengths = []
# for i in range(len(colors)):
#   min_length, max_length = min(i + 1, 2), i + (0 if i > 1 else 1)
#   lengths.append(common.randint(min_length, max_length))

# seed bluteforcer
# import sys
# from random import *;R=randrange;
# TARGET = {(13,17,4,1,2,2,2,4,3,1,6),(18,18,8,1,2,2,3,0,4,2,1),(19,19,1,1,2,2,2,3,5,1,8,3,6,2,4),(18,18,3,1,2,2,3,3,2,6,7,8,2,1,4)}
# SMTARGET = {(13,17,4),(18,18,8),(19,19,1)}
# for s in range(0+int(sys.argv[1]),175634280000,8):
#  if s//8 % 10000000 == 0: print(s)
#  seed(s);w,h,b=13+R(7),13+R(7),1+R(9)
#  HWB = (h,w,b)
#  if HWB!=(13,17,4)and HWB!=(18,18,8)and HWB!=(19,19,1)and HWB!=(18, 18, 3): continue
#  c=sample([*range(10)],a:=4+R(3))
#  l=[1+(0<i)+R(max(1,i-1))for i in range(a)]
#  generated = (h,w,b,*l,*c)
#  if generated in TARGET:
#   with open(f"tmp/{','.join(map(str,generated))}", "a") as f:
#     f.write(str(s) + "\n")
#   print(s, generated, flush=True)

# import zlib
# A=[*map(str.split, filter(len,open("tmp/s_13,17,4,1,2,2,2,4,3,1,6","r").readlines()))]
# B=[*map(str.split, filter(len,open("tmp/s_18,18,8,1,2,2,3,0,4,2,1","r").readlines()))]
# C=[*map(str.split, filter(len,open("tmp/s_18,18,3,1,2,2,3,3,2,6,7,8,2,1,4","r").readlines()))]
# D=[*map(str.split, filter(len,open("tmp/s_19,19,1,1,2,2,2,3,5,1,8,3,6,2,4","r").readlines()))]
# 285 ('{[0dr*)','oa}4e*)',']re4if)','oauloaa)')
# 285 ('{[0dr*)','{[[sraa)','41*l}{','oauloaa)')
# 285 ('*{[}-34','*{[d}4','41*l}{','uus)(*3')  337
# 285 (']2eli[[',']24l+)[','41*l}{','df(rs4*') 337
# 285 (']2eli[[',']24l+)[','41*l}{','uus)(*3') 337
# 285 (']2eli[[',']24l+)[','41*l}{','f(3,+e[') 339
# 285 (']2eli[[','41-efe[','41*l}{','f(3,+e[') 339
# 285 ('l{(foe[','41-efe[','41*l}{','f(3,+e[') 337
# 285 ('3{s+fe[','41-efe[','41*l}{','uus)(*3') 339
# 285 ('3{s+fe[','41-efe[','41*l}{','f(3,+e[') 337
# 285 ('+u-)+e[','41-efe[','41*l}{','f(3,+e[') 336
# 285 ('{di{ee[','41-efe[','41*l}{','f(3,+e[') 339
# mn = 1000
# for a in A:
# 	for b in B:
# 		for c in C:
# 			for d in D:
# 				payload = f"""from	random	import*
# def	p(f,s=4):
# seed([2024-s,'{a}','{b}','{c}','{d}'][s*(0<s)]);g,t,d=randrange(13,20)==len(f[2]),randrange(13,20)==len(f),randrange(1,10);u=sample([*{{*range(1,10)}}^{{d*(s<0)}}],a:=4+randrange(3));e=[randrange(1+(0<i),1+(i<2)+i)for	i	in	range(a)];o=[(2*a-1)*[d]for	i	in	range(a)]
# for	i	in	range(a):
# 	for	l	in	range(e[i]):l-=i;o[l-1][a+i-1]=o[l-1][a-i-1]=o[-i-1][a+l-1]=o[-i-1][a-l-1]=u[i]
# return	all([g,t,{{*sum(f,[])}}=={{*u,d}},d	in	f[2]])and	o+o[:-1][::-1]or	p(f,s-1)"""
# 				e = zlib.compress(payload.encode(), level=9)
# 				if len(e) <= mn:
# 					mn = len(e)
# 					print(mn, (a,b,c,d))

from	random	import	*
def	p(f,s=4):
	seed([2024-s,'+u-)+e[','41-efe[','41*l}{','f(3,+e['][s*(0<s)])
	g,t,d=randrange(13,20)==len(f[0]),randrange(13,20)==len(f),randrange(1,10)
	u=sample([*{*range(1,10)}^{d*(s<0)}],a:=randrange(4,7))
#	l=[1+(0<i)+randrange(max(1,i-1))for	i	in	range(a)]
	e=[1+randrange(0<i,(i<2)+i)for	i	in	range(a)]
	o=[(a*2-1)*[d]for	i	in	range(a)]
	for	i	in	range(a):
		# for	l	in	range(e[i]):o[-1-i][a-1-i+l]=o[l-1-i][a-1-i]=o[-1-i][a-1+i-l]=o[l-1-i][a-1+i]=u[i]
		for	l	in	range(e[i]):l-=i;o[l-1][a+i-1]=o[l-1][a-i-1]=o[-i-1][a+l-1]=o[-i-1][a-l-1]=u[i]
#	return	any([h^len(g),w^len(g[2]),{*sum(g,[])}^{b,*c},b	not	in	g[2]])and	p(g,s+1)or	o+o[:-1][::-1]
	return	all([g,t,{*sum(f,[])}=={*u,d},d	in	f[2]])and	o+o[:-1][::-1]or p(f,s-1)
