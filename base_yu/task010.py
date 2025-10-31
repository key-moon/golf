# 類題:254
# best: 66(Code Golf International) / others: 67(jailctf merger), 67(ox jam), 68(jacekw Potatoman nauti natte), 68(import itertools), 70(4atj sisyphus luke Seek mukundan)
# ============================== 66 ==============================
# p=lambda g:[*zip(*[[x and 9-sorted(map(sum,zip(*g))).index(sum(s))for x in s]for s in zip(*g)])]
# p=lambda g:[*zip(*[[x and 9-sorted(zip(*g),key=sum).index(s)for x in s]for s in zip(*g)])]
# p=lambda g:[[x and 9-sorted(zip(*g),key=sum).index(t)for x,t in zip(s,zip(*g))]for s in g]
p=lambda g:[[x and 9-sorted(zip(*g),key=sum).index((*t,))for*t,x in zip(*g,s)]for s in g]
# p=lambda g:(u:=[*zip(*g)])and[[s.pop(0)and 9-sorted(u,key=sum).index(t)for t in u]for s in g]
