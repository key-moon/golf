# best: 62(jailctf merger) / others: 64(Code Golf International), 64(intgrah jimboko awu macaque sammyuri), 65(4atj sisyphus luke Seek mukundan), 65(LogicLynx), 65(ox jam)
# lambda g,R=[0]*99,S=[0]*99:eval(str([S:=[(c<1)*(D&3)+7*(c>0==C==D)for c,C,D in zip(r,R,S)if(R:=r)]for r in g]).replace(*"70"))

# C c D
# == 縁への侵入 == 侵入時点で色をつける 脱出前に色を消す
# 0 2 0 -> ?
# 0 2 3 -> 0
# == 縁からの脱出 == 
# 2 0 0 -> 0
# 2 0 ? -> 3
# == 通常 == 
# 0 0 0 -> 0
# 0 0 3 -> 3
# == 縁 == 色を消さないと、縁からの脱出時点で判定が狂う
# 2 2 0 -> 0
# 2 2 ? -> 0

# c==0 -> D&3
# c==2 -> C==D==0 * 5
# lambda g,R=[0]*99:(S:=R)and eval(str([S:=[(c<1<D)*3+7*(c>1>C+D)for c,C,D in zip(r,R,S)if(R:=r)]for r in g]).replace(*"70"))

# -- or --

# c D
# == 縁への侵入 == 侵入時点で特殊色（次を3に）、脱出前に別の色
# 2  0 ->  ?
# 2  3 -> -?
# 2  ? -> -?
# 2 -? -> -?
# == 縁からの脱出, 通常 ==
# 0 0 -> 0
# 0 ? -> (0<?)*3
# lambda g,S=[0]*99:eval(str([S:=[0**c*D%4+c//~c*(3*(2<D)-7)for c,D in zip(r,S)]for r in g]).replace(*"70").replace(*"40"))
# ?: 1
# lambda g,S=[0]*99:eval(str([S:=[[3*(0<D),1-2*(0!=D)][1<c]for c,D in zip(r,S)]for r in g]).replace(*"10"))
# [[3*(0<D),1-2*(0!=D)][1<c]
# [[1,-1],[0,1,0]][1<c][D]
# ?: 0.5
# ============================ 62 ============================
p=lambda g:[(D:=0)or[int(D:=[3*(0<D),.5-(0!=D)][1<c])for c in r]for r in g]

# 別案:
# lambda g:[(D:=0)or[(D:=[3*(0<D),4-8*(0!=D)][1<c])&3for c in r]for r in g]
