import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((0xdeadbeef * 5 + (ord(char) + 29) % 256) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()