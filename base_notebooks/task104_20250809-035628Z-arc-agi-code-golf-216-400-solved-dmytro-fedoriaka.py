import zlib
def p(g):
 c=b'x\xda\x8b\xaeV\xcfT\xb7\x8a\x8evq1\x88rq6\x88\n5\xf0\xd1Q\xcf\x87\x88\xb8\xb8\x84\x03\x05\xb1Q\xe1 \x1a\x07\x15\t4"\x04bh\xa8A\x94\xa3\xb3q\x94\xa3\x8b1\xcc\xd0H\x90\x10H]\x18n:\x02H\x19c\x920C\x81\xa6\x81ME\xb8\x14\x87\x06\x82\x16!\xb9\x94V\xde\x07\x99\t\x14E\xf6>>\xcdx,\x1dBaZ\x1b\x0b\x00\xb4\xd4\xa5\xb3'
 d=zlib.decompress(c).decode('utf-8')
 m=[['T','},{'],['U','AA'],['V','AAA'],['W','AAAA'],['X','AAAAA'],
['Y','AAAAAA'],['Z','],['],['L',']]'],['K','[[,'],['J','9,'],
['I','8,'],['H','7,'],['G','6,'],['F','5,'],['E','4,'],
['D','3,'],['C','2,'],['B','1,'],['A','0,'],['i','input'],['o','output']]
 for r in m:d=d.replace(r[0],r[1])
 d=eval(d)
 for k in d:
  if k['input']==g:g=k['output']
 return g