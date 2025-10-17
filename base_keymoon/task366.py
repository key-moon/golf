# best: 358(jailctf merger) / others: 365(ox jam), 371(4atj sisyphus luke Seek mukundan), 372(kambarakun), 374(Tony Li), 374(sekken)
# とりあえずあんまgolfのこと考えずに愚直に書く
from re import *;s=sub
def p(g):
 # TODO: カスのコーナーケース対処をなんとかする 
 # 反転させないと110で
 # x. .x
 # xx ..
 # ..
 # みたいなやつが侵食して死ぬ subを1にするのと
 h=len(g:=g[::-1])
 w=len(g[0])
 a,b=([l[:w//2]for l in g],[l[w//2:]for l in g])if h<w else(g[:h//2],g[h//2:])
 if h<w:w=w//2
 # 要素数が少ないほうがテンプレート aがテンプレート bがパズルのピーズ
 if len(set(str(a)))>len(set(str(b))):a,b=b,a
 A=s("[[ ,]","",str(a))+"0"*w
 B=s("[[ ,]","",str(b))
#  print("B:")
#  print(*B.replace("]","\n").splitlines()[:-2], sep="\n")
 c=max(B,key=B.count)
 d=max(B:=s("]",c,B),key=s(c,"",B).count)
 # print(f"{CASE=} puzzle base: {c} puzzle piece base: {d}")
 # u=sum(([*findall(f"([^{c}]{{{j}}}){"."*(w-j+1)}"*i,B)]for i in range(2,h) for j in range(2,w)),[])
 # findallなのは同じshapeのピースが複数ある場合があるから
 # 含まれてるドットが多いほうから探索するためソート（そうしないと、包含関係にあるやつがあるせいで破滅する）
 # 最初はパターンに内包されるパターンも拾ってきてたんだけど、いろいろ問題がおきる
 # 例えば何も含まれてないパターンで全体が塗りつぶされるとか、角が内包されるパターンで侵食されるとかそういうやつ
 # 仕方なく番兵を入れた
 # TODO: sortのkeyマシになんないかな
#for l in sorted(sum(([*findall(f"(?={c}.{{{w-2}}}"+f"{c}([^{c}]{{{2+i%w}}}){c}.{{{w-3-i%w}}}"*(2+i//w)+f".{c})",2*c*w+B+2*c*w)]for i in range(h*w)),[]),key=lambda x:str(x).count(d)*0.99-sum(map(len,x))):
 for l in sorted(sum(([*findall(f"(?={c}.{{{w-2}}}"+f"{c}([^{c}]{{{j}}}){c}.{{{w-1-j}}}"*i+f".{c})",2*c*w+B+2*c*w)]for i in range(2,h)for j in range(2,w)),[]),key=lambda x:str(x).count(d)*0.99-sum(map(len,x))):
  l=[*l]
  t="."*(w-len(l[0])+1)
  p=""
  while l:
   u=l.pop()
   A=s(s(d,f"[^]{c+d}]",f"(?<={t.join([*l,''])}){u}(?=")+p+")",u,A,1)
   p=t+u+p
  A=s(d,c,A)
 return [[*map(int,r)]for r in s(c,d,A).split("]")[-3::-1]]#  s.sort(key=lambda x:x.groups())
