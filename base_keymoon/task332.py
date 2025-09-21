# best: 58(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 61(ox jam), 61(xsot ovs att joking mewheni), 64(jacekw Potatoman nauti), 64(jacekwl Potatoman nauti), 66(intgrah jimboko awu macaque sammyuri)
# lambda g:[(a:=[1,.6])and[c*(a:=a[::-1])[0]for c in r[::-1]][::-1]for r in g]
# lambda g:[[c*[1,.6][i+len(r)&1]for i,c in enumerate(r)]for r in g]
# lambda g:[(a:=5)and[(0<c)*(a:=a^6)for c in r[::-1]][::-1]for r in g]
# lambda g:[[(0<c)*(a:=a^6)for c in r]for r in g if(a:=3^6*len(r)%12)]
# lambda g:[(a:=.6+.8*len(r)%1.6)and[c*(a:=1.6-a)for c in r]for r in g]
# lambda g:[[v*.6**(len(s)-i&1)for i,v in enumerate(s)]for s in g]
# ========================== 58 ==========================
p=lambda g:[eval("7**len(r)*r.pop(0)%8,"*len(r))for r in g]

# b*7**a%8
# b*7**a%8
# mappings = {
#     (0,0): 0,
#     (1,0): 0,
#     (2,0): 0,
#     (3,0): 0,
#     (4,0): 0,
#     (5,0): 0,
#     (0,5): 5,
#     (2,5): 5,
#     (4,5): 5,
#     (1,5): 3,
#     (3,5): 3,
#     (5,5): 3,
# }
