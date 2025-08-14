# 罠: 中央のドットは背景と同じ色のことがある
# 矩形が交わってることがある
# ひどいケース(67):
#|  +       +  
#|* ++**   ++  
#|   . *       
#|   .         
#|   ...     ..
#+-------------
#これで正規表現によるマッチが不可能になる
import re
def p(g):
 t=str(g)
 # 中心かそれ以外か
 c=min(t,key=t.count)
 b=max(t,key=t.count)
 # 中心は同じ色のケースがある
 c=[c,b][t.count(c)<2]
 
 t=str([*g,*zip(*g)])
 # 反転して足してるのは * ++** + 片側からかしかマッチできないケースがあるから
 # 360度全部試すのと同じ
 t=re.sub("[([ ,]","",t+t[::-1])
 SEQS = [ANSWER[i][i] for i in range(len(ANSWER)//2+1)[::-1]]
 # ****   ****
 # (\1\1+)
 # (\1{{{2,}}})
 a = re.findall(rf"([^{b}])+" "([^)\\]]+?)" "(\\1\\1+)",t)
 s=[]
 print(a)
 # .......
 #  .....
 #   ...
 #    .
 l=sorted([b*len(s)+z+b*len(y)+z for x,y,z in a if (x not in s and (s:=[*s,x]))],key=len)
 
 print("\n".join("".join(map(str,r)).replace(b," ") for r in g))
 print(l)
 input("> ")
 
 if len(SEQS) - 2 != len({*(a for a, b in a)}):
  print(f"{CASE=}")
  print(t)
  print(a, ({*(b for a, b in a)}))
  input("> ")
  return
 return ANSWER
#  if len(ANSWER)//2-1==len(a):
#   return ANSWER
#  if CASE < 5:
#   print(CASE)
#   print(a)
 