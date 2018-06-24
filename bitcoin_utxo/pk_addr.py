
import binascii
import segwit_addr

def hextobytes(h):
    d = binascii.unhexlify(h)
    r = []
    for c in d:
        r = r + [ord(c)]
    return r

def bytestohex(bl):
    d = b''
    for b in bl:
        d = d + chr(b)
    return binascii.hexlify(d)

def pk_encode(k):
    pk8 = hextobytes(k)
    pk5 = segwit_addr.convertbits(pk8,8,5)
    a = segwit_addr.bech32_encode('pk',pk5)
    return a

def pk_decode(a):
    (hrp, pk5) = segwit_addr.bech32_decode(a)
    if hrp != 'pk':
        return None
    pk8 = segwit_addr.convertbits(pk5,5,8)
    if len(pk8) < 33:
        return None
    if len(pk8) > 33:
        for b in pk8[33:]:
            if b > 0:
                return None
        pk8 = pk8[0:33]
    return bytestohex(pk8)