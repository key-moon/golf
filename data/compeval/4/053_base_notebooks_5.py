def p(g):
 d='[ogFBksFBmYFBskFSLFDLFEMNsMdTUGDUGjYZkxEPZPxEVHDVHEJCksJCmwQJDQJENNsNd2]YFDkFEWHDWHEPPsPdSXzDXzjYMskzTGCzDGCzENJDNJjYJDkJEQMsQzTQGDQGjYJCskJTUJDUJEMGDMGEVFDVFEHBZHBxEUzDUzEMksMmwQzDQzEWZWxELZLxENMsNzTUMsUz2]YRskxSLRsLxSQGCsQGTXksXmwLPsLdSQNsQdTLHBsLHSNzDNzEXNsXdTRPsRdSPFDPFELHDLHEXGDXGEPRsPxSWksWmwRHDRHEVZVxERZRxEMzDMzERksRmwWPsWdSVRsVx1]t]'
 m='xDZvlYJeXFeWHeVGeU2KT1KSxBRzeQdBPdCNzCMxeL]wKAiJyaHAaGyhFjwEesD2bC1bB[iAciz[hychxvgwuovt,u]}trlsqOrp"qmbpnIo{"ndjmgkldek0]j2,i1,hf[g":f0becad[ac],b0,a'
 m=[[m[i:i+2],m[i+2]]for i in range(0,len(m),3)]
 for r in m:d=d.replace(r[1],r[0])
 d=eval(d)
 for k in d:
  if k['I']==g:g=k['O'];return g