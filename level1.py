#!/usr/bin/env python3

import string

cipher_text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq 
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq 
rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu 
ynnjw ml rfc spj.""" 

# Make translation table from alphabet to alphabet + 2 positions
frm = string.ascii_lowercase
to = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
trans_table = string.maketrans(frm, to)
plain_text = string.translate(cipher_text, trans_table)
print(plain_text)

# Translate the url
url = 'http://www.pythonchallenge.com/pc/def/.html'
url_part = 'map'
translated_part = string.translate(url_part, trans_table)
print('http://www.pythonchallenge.com/pc/def/%s.html' % translated_part)
