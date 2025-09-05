# best: 146(4atj sisyphus luke Seek) / others: 148(mukundan), 161(jailctf merger), 178(xsot ovs att joking mewheni), 234(MasukenSamba), 236(duckyluuk)
# ===================================================================== 146 ======================================================================

# def p(g):
#     H, W = len(g), len(g[0])
#     x = ({*sum(g, [])} - {0, 2}).pop()
#     Y, X = next((r, c) for r in range(H - 1) for c in range(W - 1)
#                 if 0 not in (g[r][c], g[r+1][c], g[r][c+1], g[r+1][c+1]))
#     p_vals = [r + c for r in (Y, Y + 1) for c in (X, X + 1)]
#     m_vals = [r - c for r in (Y, Y + 1) for c in (X, X + 1)]
#     p_min, p_max = min(p_vals), max(p_vals)
#     m_min, m_max = min(m_vals), max(m_vals)
#     result = [[0] * W for _ in range(H)]
#     for r in range(H):
#         for c in range(W):
#             is_in_box = (Y <= r <= Y + 1) and (X <= c <= X + 1)
#             ext_tr = (g[Y][X+1] == 2 and 
#                       p_min <= r + c <= p_max and 
#                       r <= Y and c >= X + 1)
#             ext_bl = (g[Y+1][X] == 2 and 
#                       p_min <= r + c <= p_max and 
#                       r >= Y + 1 and c <= X)
#             ext_tl = (g[Y][X] == 2 and 
#                       m_min <= r - c <= m_max and 
#                       r <= Y and c <= X)
#             ext_br = (g[Y+1][X+1] == 2 and 
#                       m_min <= r - c <= m_max and 
#                       r >= Y + 1 and c >= X + 1)
#             if is_in_box or ext_tr or ext_bl or ext_tl or ext_br:
#                 result[r][c] = x        
#     return result

# 圧縮よくわからん

def p(g):
 Y,X=next((r,c)for r,R in enumerate(g[:-1])for c,C in enumerate(R[:-1])if C*g[r+1][c]*R[c+1]*g[r+1][c+1])
 return[[[0,({*sum(g,[])}-{0,2}).pop()][0<=r-Y<2 and 0<=c-X<2 or g[Y+(r>Y)][X+(c>X)]==2 and[(r-c-Y+X)**2<2,0<=r+c-Y-X<3][(r>Y)^(c>X)]]for c,_ in enumerate(R)]for r,R in enumerate(g)]
