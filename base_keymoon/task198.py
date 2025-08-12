# best: 127 信じられねえ
# 連結成分は 4、無は3
# マスのサイズは3か4
# (偶然) max(g[5]) で仕切りを検出できる 冷静になると max(g)[0] でもできる
# 穴は2ます以上の場合もある 縦に3ます穴が空いている場合もある（ケース148）

# regex golfの残骸（コーナーケースに対処できずに伸びに伸びたゴミ、勝ち方針はregexではないと思う）
import re;s=re.sub
def p(g):
 a="."*len(g)
 d=a+"]"+s("[[ ,]","",str(g))+a
 v=f"[.{max(d.replace("0",""),key=d.count)}\]]"
 for x in d:
  d=s(f"0(?=({a})?4)","4",s(f"(?<={v+a}{v+a})0(?=({a}0)?({a}0)?{a+v})|(?<={v+a})0(?=({a}0)?{a+v})|(?<={v})0(?=0?{v})","4",d))[::-1]
 return[[*map(int,r)]for r in s("0","3",d).split("]")[1:-2]]

# def p(g):
#  h=len(g);r=range(h-1);a=max(g)[0]
#  for _ in g[1:]:
#   [for c in r]for 
#   g=eval(str(g)[::-1])
 
#  return eval(str(g).replace("0","3"))
