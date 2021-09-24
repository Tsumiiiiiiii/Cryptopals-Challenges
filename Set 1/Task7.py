from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
from Crypto.Cipher import AES

with open('7.txt') as input_file:
  ciphertext = b64decode(input_file.read())

key = b"YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
