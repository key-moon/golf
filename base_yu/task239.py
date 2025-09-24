# best: 99(ox jam) / others: 105(4atj sisyphus luke Seek mukundan), 105(natte), 105(jailctf merger), 106(intgrah jimboko awu macaque sammyuri), 110(HETHAT)
# =============================================== 99 ==============================================
# f p(g):u=sum(g,[]);C=sorted([(-u.count(v),v)for v in{*u}]);return[*zip(*[[c]*-v+[0]*(v-min(C)[0])for v,c in C])]
# f p(g):u=sum(g,[]);C=sorted({*u},key=(k:=u.count))[::-1];return[*zip(*[[c]*k(c)+[0]*(k(C[0])-k(c))for c in C])]
# def p(g):u=sum(g,[]);C=sorted({*u},key=(k:=u.count))[::-1];return[[c*(i<k(c))for c in C]for i in range(k(C[0]))]
# def p(g):u=sum(g,[]);C=sorted([[c:=u.count(v)]+[v]*c+[0]*99for v in{*u}])[::-1];return[*zip(*C)][1:C[0][0]+1]
def p(g):u=sum(g,[]);C=sorted([c:=-u.count(v)]+[v]*-c+[0]*99for v in{*u});return[*zip(*C)][1:1-C[0][0]]
