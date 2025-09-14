# best: 78(jailctf merger) / others: 81(4atj sisyphus luke Seek mukundan), 82(xsot ovs att joking mewheni), 125(MasukenSamba), 126(intgrah jimboko awu macaque sammyuri), 143(Afordancja)
# ==================================== 78 ====================================
# lambda g:[[v^(max(t)&max(s))-v&2for*t,v in zip(*g,s)]for s in g]
# lambda g:[[v|min(max(t),max(s))-v&2for*t,v in zip(*g,s)]for s in g]
p=lambda g:[[v^(max(s)&max(t)+7*0**(hash((*t,))%5647))>>-~v for*t,v in zip(*g,s)]for s in g]

# { (0,0): 0, (0,1): 1, (1,1): 3, (1,8): 8, }
# (min(max(t),max(s)),v): { (0,0): 0, (1,0): 0, (1,1): 1, (8,1): 3, (8,8): 8 }
# (max(t)&max(s),v): { (0,0): 0, (0,1): 1, (1,0): 0, (1,1): 1, (8,1): 3, (8,8): 8 }

# エッジケース列↓
# (0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1)
