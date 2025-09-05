# best: 78(jailctf merger) / others: 82(mukundan), 86(4atj sisyphus luke Seek), 114(xsot ovs att joking mewheni), 163(duckyluuk), 164(Jonas)
# ==================================== 78 ====================================
# lambda g:[[v^(max(t)&max(s))-v&2for*t,v in zip(*g,s)]for s in g]
# lambda g:[[v|min(max(t),max(s))-v&2for*t,v in zip(*g,s)]for s in g]
p=lambda g:[[v^(max(s)&max(t)+7*0**(hash((*t,))%5647))>>-~v for*t,v in zip(*g,s)]for s in g]

# { (0,0): 0, (0,1): 1, (1,1): 3, (1,8): 8, }
# (min(max(t),max(s)),v): { (0,0): 0, (1,0): 0, (1,1): 1, (8,1): 3, (8,8): 8 }
# (max(t)&max(s),v): { (0,0): 0, (0,1): 1, (1,0): 0, (1,1): 1, (8,1): 3, (8,8): 8 }

# エッジケース列↓
# (0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1)
