# best: 53(HIMAGINE THE FUTURE.) / others: 59(jailctf merger), 64(Code Golf International), 64(4atj sisyphus luke Seek mukundan), 67(biz), 68(ox jam)
# lambda g:g*0!=0and[*map(p,((a:=g[:len(g)//2])*2==g)and a or g)]or g <- failed
# キショすぎケース: 全部単色縦横偶数
# lambda g:[a:=g[:len(g)//2],[s[:len(s)//2]for s in g]][a*2!=g] <- failed
# キショすぎケース2: (2*2)x4
# lambda g:[g[:(h:=len(g)//2)],[s[:(w:=len(s)//2)]for s in g]][h<w]
# lambda g:[g[:(h:=len(g)//2)],[s[:(w:=len(s)//2)]for s in g]][g[0]!=g[h]or h<w]
# lambda g:[a:=g[:(h:=len(g)//2)],[s[:(w:=len(s)//2)]for s in g]][g!=a*2or h<w]
# f p(g):h=len(g)//2;return[a:=g[:h],[s[:len(s)//2]for s in g]][g!=a*2or h<2]
# lambda g:[a:=g[:(h:=len(g))//2],[s[:len(s)//2]for s in g]][g!=a*2or h<3]
# lambda g:[a:=g[:53%~-len(g)],[s[:len(s)//2]for s in g]][g!=a*2]
# ======================== 53 =======================
p=lambda g:g==(a:=g[:53%~-len(g)])*2and a or[*map(p,g)]
# mapping = { 2: 0, 4: 2, 6: 3, 8: 4 }
