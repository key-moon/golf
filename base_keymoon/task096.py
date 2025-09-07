# best: 325(xsot ovs att joking mewheni) / others: 396(jailctf merger), 442(dbdr), 449(jacekwl Potatoman), 449(jacekwl), 503(J&R)
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


# optimal: 353
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
