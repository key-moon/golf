# best: 159(jailctf merger, biz) / others: 161(4atj sisyphus luke Seek mukundan), 169(intgrah jimboko awu macaque sammyuri), 172(ox jam), 181(import itertools), 205(THUNDER THUNDER)
# ============================================================================ 159 ============================================================================
# port re;S=re.sub;l=lambda g,c:g*c or[*zip(*l(eval(S("1, 8", "1, 1",str(l(g,c+1)))),c+1))][::-1];p=lambda g,c=[]:0**("8"in str(g))*c or p(l(S(*'81',str(g),1),-23),[[8-sum(v),*v]for v in[[0]*len(c)]+c])
# str.replace;l=lambda g,c=:g*c or[*zip(*l(eval(S(str(l(g,c+1)),"1, 8", "1, 1")),c+1))][::-1];p=lambda g,c=[]:0**("8"in str(g))*c or p(l(S(str(g),*'81',1),-23),[[8-sum(v),*v]for v in[[0]*len(c)]+c])
# lambda g,c:-c*g or[*zip(*eval(str(l(g,c-1)).replace("1, 8","1, 1")))][::-1];p=lambda g,c=[]:c*0**("8"in str(g))or p(l(str(g).replace(*'81',1),23),[[8-sum(v),*v]for v in[[0]*len(c)]+c])
# lambda g,c:-c*g or[*zip(*eval(str(l(g,c-1)).replace(*["1, 8","8","1, 1","1"][c<1::2],1)))][::-1];p=lambda g,c=[]:c*0**("8"in str(g))or p(l(g,23),[[8-sum(v),*v]for v in[[0]*len(c)]+c])
# lambda g,c:-c*g or[*zip(*eval(str(l(g,c-1)).replace("1, 8"[(b:=3*0**c):],"1, 1"[b:],1)))][::-1];p=lambda g,c=[]:c*0**("8"in str(g))or p(l(g,23),[[8-sum(v),*v]for v in[[0]*len(c)]+c])
l=lambda g,c:-c*g or[*zip(*eval(str(l(g,c-1)).replace((b:=(c>0)*"1, ")+"8",b+"1",1)))][::-1];p=lambda g,c=[]:c*0**("8"in str(g))or p(l(g,23),[[8-sum(v),*v]for v in[[0]*len(c)]+c])


# 連結成分の個数がほしい ref: base_keymoon/task048.py
# import re;s=re.sub
# def p(g):
#  d=s("[[ ,]","",str(g))
#  n=[8]
#  while"8"in d:
#   d=s("8","1",d,1)
#   for x in d:
#    d=s("8(?=("+"."*len(g[0])+")?1)","1",d)[::-1]
#   n+=[0]
#  # ここ割と適当 改善の余地あるかも
#  return [(n:=[0,*n[:-1]])[1:]for x in n[:-1]]
