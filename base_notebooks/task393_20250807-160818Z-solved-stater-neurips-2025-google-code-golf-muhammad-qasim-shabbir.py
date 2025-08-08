from collections import*
def p(g):h,w=len(g),len(g[0]);f=[i for s in g for i in s];C=Counter(f).most_common(4);C=[c for c in C if c[0]>0];g=[[c[0]]for c in C];return g