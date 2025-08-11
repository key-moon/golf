import re;s=re.sub
def p(g):
 a=s("[[ ,]","",str(g))
 for i in range(1,9):
  pat = re.compile(rf"({i}[^\]]*?)0(?=[^\]]*{i})")
  # 0 を i に、左側は \1 で戻す
  a = pat.sub(rf"\1{i}", a)
 return [[*map(int,r)]for r in a.split("]")[:-2]]
