# best: 90(4atj sisyphus luke Seek mukundan) / others: 91(ox jam), 91(intgrah jimboko awu macaque sammyuri), 96(HETHAT), 97(cubbus), 97(2F)
# ========================================== 90 ==========================================
# port re;S=re.sub;p=lambda g,c=-63:c*S(*"04",str(g))or eval(S(*"90",str(p(eval(S("0(?=, 9|\))","9",str([*zip(*g[::-1])]))),c+1))))
# port re;S=re.sub;p=lambda g,c=-63:g*c or eval(S(*"0940"[c<0::2],str(p(eval(S("0(?=, 9|\))","9",str([*zip(*g[::-1])]))),c+1))))
# port re;S=re.sub;p=lambda g,c=-63:c*S(" 0,"," 4,",str(g))or p(eval(S(" 0(?=, 0\.|\))",".0",str([*zip(*g[::-1])]))),c+1)
# port re;S=re.sub;p=lambda g,c=-63:c*S(*"04",str(g))or[*zip(*eval(S("4(?=, 0|\))","0",str(p(g,c+1)))))][::-1]
# port re;p=lambda g,c=-63:c*g or[*zip(*eval(re.sub(*["4(?=, 0|\))",*"004"][c>-1::2],str(p(g,c+1)))))][::-1]
# 初手で0を4にする そのあとに0で塗り拡げ
import re;p=lambda g,c=63:-c*g or[*zip(*eval(re.sub(*["4(?=, 0|\))",*"004"][c<1::2],str(p(g,c-1)))))][::-1]
