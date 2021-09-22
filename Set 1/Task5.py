from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
from string import printable

a = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

k = "ICE"

cipher = bytes(a, "utf-8")
key = bytes(k, "utf-8")

s, idx = [], 0

for i in cipher:
  s.append(int(i) ^ key[idx])
  idx = (idx + 1) % len(key)

print(hexlify(bytes(s)))
