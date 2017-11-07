import sys
 
#Suppose you are told that the one time pad 
#encryption of the message "attack at dawn" 
#is 09e1c5f70a65ac519458e7e53f36 
#(the plaintext letters are encoded 
#    as 8-bit ASCII and the given ciphertext
# is written in hex). What would be the one 
#time pad encryption of the message "attack 
#on titan" under the same OTP key?
 
 
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
 
def random(size=16):
    return open("/dev/urandom").read(size)
 
def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c
 
def printAscii(msg):
    z = [chr(ord(x)) for x in msg] 
    x = "".join(z)
    print x.encode('hex')
 
def main():
    text = "attack on titan"
  
    
    enc = "09e1c5f70a65ac519458e7e53f36".decode('hex')
    key = strxor(text, enc)
 
 
    text2 = "attack on titan"
    enc2 = strxor(text2, key)
 
    print enc2.encode('hex')
 
 
 
main()
