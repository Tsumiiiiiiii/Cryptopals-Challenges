from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
from string import printable

opts = printable

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



f = open("t4.txt", "r")
stuff = []

for line in f.readlines():
  cipher = unhexlify(line.strip())
  for key in opts:
    s = []
    for ch in cipher:
      s.append(int(ch) ^ ord(key))
    para = bytes(s)
    score = get_english_score(para)
    stuff.append([score, para])

stuff.sort(reverse=True)
print(stuff[0])
