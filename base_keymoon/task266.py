# best: 98(jailctf merger, HIMAGINE THE FUTURE.) / others: 102(ox jam), 102(THUNDER THUNDER), 102(biz), 109(import itertools), 114(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ============================================== 98 ==============================================
# port re;p=lambda g,c=3:-c*g or[*zip(*eval(re.sub("0(?=.{%s}2)"%(19-c%2*6),"(-c^3)%10",str(p(g,c-1)))))][::-1] <- 2 のreplaceができてないやつ
# lambda g,A=[0]*9+[3,0,6]+[0]*7+[8,0,7]+[0]*9:[A[15-sum(g,[]).index(2)+i:][:5]for i in(0,5,10)] <- wraparound忘れてた カス
# lambda g,A=[b:=(a:=[0]*3)*3,a+[3,0,6]+a,b,a+[8,0,7]+a,b]:[r[4-max(g).index(2):][:5]for r in A[2-g.index(max(g)):]]
# lambda g,a=[0]*3:[r[4-max(g).index(2):][:5]for r in[a*3,a+[3,0,6]+a,a*3,a+[8,0,7]+a,a*3][2-g.index(max(g)):][:3]]
# f p(g,a=[0]*3):m=max(g);return[r[4-m.index(2):][:5]for r in[a*3,a+[3,0,6]+a,a*3,a+[8,0,7]+a,a*3][2-g.index(m):][:3]]
# lambda g,a=[0]*3:[r[4-max(g).index(2):][:5]for r in[a*3,a+[3,0,6]+a,a*3,a+[8,0,7]+a,a*3][2-g.index(max(g)):][:3]]
# p=lambda g,A=(a:=[0]*17)+[3,0,6]+a+[8,0,7]+a:[A[i-(a:=sum(g,[]).index(2))-a//5*5:][:5]for i in b"\x1c\x26\x30"]
# p=lambda g,A=(a:=[0]*17)+[3,0,6]+a+[8,0,7]+a:[A[i-(a:=sum(g,[]).index(2))*2+a%5:][:5]for i in b"\x1c\x26\x30"]
a=[0]*17
p=lambda g:[(a+[3,0,6]+a+[8,0,7]+a)[i-(b:=sum(g,[]).index(2))*2+b%5:][:5]for i in b"\x1c\x26\x30"]

# mapping = { 0: 3, 1: 6, 2: 7, 3: 8, 4: 0 }
# mapping = { 0: 0, 1: 8, 2: 7, 3: 6, 4: 3 } a*8%29%9
