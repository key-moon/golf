# best: 105(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, jailctf merger, biz) / others: 106(HIMAGINE THE FUTURE.), 106(intgrah jimboko awu macaque sammyuri), 107(ox jam), 117(Code Golf International), 117(4atj sisyphus luke Seek mukundan)
# ================================================= 105 =================================================
# port re;p=lambda g:eval(r'(g:=eval(re.sub("1, 1, 1(.{25})1, 0, 1(.{25})1, 1, 1",r"0,2,0\1 2,2,2\2 0,2,0",str(g)))),'*2)[1]
# port re;p=lambda g,c=-2:g*c or eval(re.sub("(1, 1, 1)(.{25})1, 0, 1(.{25})\\1",r"0,2,0\2 2,2,2\3 0,2,0",str(p(g,c+1))))
# port re;p=lambda g,c=-2:g*c or eval(re.sub("1, ., 1(.{25})?"*3,r"0,2,0\1 2,2,2\2 0,2,0\3",str(p(g,c+1))))
import re;p=lambda g,c=-2:g*c or eval(re.sub("1.{5}1(.{25})?"*3,r"0,2,0\1 2,2,2\2 0,2,0\3",str(p(g,c+1))))

# import re
# def p(g):
#  g=eval(re.sub("1, 1, 1(.{25})1, 0, 1(.{25})1, 1, 1","0,2,0\\1 2,2,2\\2 0,2,0",str(g)))
#  g=eval(re.sub("1, 1, 1(.{25})1, 0, 1(.{25})1, 1, 1","0,2,0\\1 2,2,2\\2 0,2,0",str(g)))
#  return g
