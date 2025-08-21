import numpy as np
def p(g):X=[x for R in g for x in R];i=len(set(X))-1;return np.kron(g,np.ones((i,i))).astype(int).tolist()