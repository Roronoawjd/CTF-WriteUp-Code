from pydoc import plain


fd = open('./DyingMessage','r')

secret = fd.read()
enc = bytes.fromhex(secret)
str = ""
for i in range(1,256):
    for j in enc:
        str += chr(i^j)
    if(str[0:3]=="DH{"):
        print(str)
        print('xor한 값 =',i) 
    str = ""