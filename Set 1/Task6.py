'''INCOMPLETE'''

from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
from string import printable

def hamming(a, b):
  a, b = bytes(a), bytes(b)
  '''a = [ord(ch) for ch in a]
  b = [ord(ch) for ch in b]
  ab, bb = "", ""
  for c in a:
    ab += bin(c)[2:]
  for c in b:
    bb += bin(c)[2:]
  diff = 0
  for cha, chb in zip(ab, bb):
    diff += (cha != chb)
  return diff #+ abs(len(ab) - len(bb))'''
  ret = 0
  for (c, d) in zip(a, b):
    diff = c ^ d
    ret += sum([1 for bit in bin(diff) if bit == '1'])
  return ret


def get_english_score(input_bytes):
    """Compares each input byte to a character frequency
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def singleXor(cipher, key):
  s = []
  for ch in cipher:
    s.append(int(ch) ^ key)
  para = bytes(s)
  return para  


with open('6.txt') as input_file:
  cipher = b64decode(input_file.read())

result = []

for keylen in range(2, 41):
  distances = []
  chunks = [cipher[i:i+keylen] for i in range(0, len(cipher), keylen)]
  idx = 0
  while True:
    try:
      chunk1, chunk2 = chunks[0], chunks[1]
      distance = hamming(chunk1, chunk2)

      distances.append(distance / keylen)

      idx += 1
      del chunks[0]
      del chunks[1]

    except Exception as e:
      break

  result.append([sum(distances) / len(distances), keylen])
  result.sort(reverse = True)

sz = result[0][1]
opts = printable

transposed = []
chunks = [cipher[i:i+sz] for i in range(0, len(cipher), sz)]

for idx in range(sz):
  result = b''
  for og in chunks:
    result += og[idx:idx + 1]
  transposed.append(result)

top_score = []

for block in transposed:
  scores = []
  for maybe in opts:
    plaintext = singleXor(block, ord(maybe))
    score = get_english_score(plaintext)
    scores.append([score, plaintext, maybe])
  scores.sort(reverse = True)
  top_score.append(scores[0][2])

key = ''.join(top_score)

cipher = b''
idx = 0
