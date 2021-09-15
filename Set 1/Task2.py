from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode

a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"

a, b = unhexlify(a), unhexlify(b)

s = []
for (p, q) in zip(a, b):
  s.append(p ^ q)
xor = hexlify(bytes(s))
print(xor)
