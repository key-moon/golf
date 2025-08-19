# 3456789012345678901234567890123456789012345678901234567890123456789
# p=lambda g:[*filter(len,[[sum({*sum(g,[])})-v for v in s if v]for s in g])]
p=lambda g:[[sum({*sum(g,s)})-v for v in s if v]for s in g if any(s)]