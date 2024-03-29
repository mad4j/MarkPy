

import os
import binascii
import hashlib

import zlib
from functools import wraps
from time import time


class Chunk:
    def __init__(self) -> None:
        self.weight = 0
        self.key = 0
        self.residual = []

    def __str__(self) -> str:
        return f'weight: {self.weight}, key: {self.key:010x} residual: {binascii.hexlify(bytearray(self.residual))}'

    def update(self, weight, key, residual) -> None:
        self.weight = weight
        self.key = key
        self.residual = residual


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

def zeros(values):
    value = 0
    for b in values:
        value += b.bit_count()
    return 8*len(values) - value


if __name__ == '__main__':

    data = os.urandom(64)
    target = zeros(data)
    data_z = zlib.compress(data, 9)

    print(f'Input data: {binascii.hexlify(bytearray(data))}')
    print(f'zeros: {zeros(data)}')
    print(f'input compressed len: {len(data_z)}')

    ck1 = Chunk()
    ck2 = Chunk()

    d1 = data[0:32]
    d2 = data[32:64]

    DOMAIN = 4

    for v in range(1 << 8*DOMAIN):

        H = hashlib.sha256(v.to_bytes(DOMAIN, 'big')).digest()

        T1 = bytes(a ^ b for (a, b) in zip(d1, H))
        T2 = bytes(a ^ b for (a, b) in zip(d2, H))

        W1 = zeros(T1)
        W2 = zeros(T2)

        if W1 > ck1.weight:
            ck1.update(W1, v, T1)
            print(f'UPDATED CK1: {ck1}')

        if W2 > ck2.weight:
            ck2.update(W2, v, T2)
            print(f'UPDATED CK2: {ck2}')

        if v % 0x100000 == 0:
            print(f'{v:010x}: max: {ck1.weight}, {ck2.weight}')
            
    print(f'RESULT: {ck1}')
    print(f'RESULT: {ck2}')

    data_z = zlib.compress(data, 9)
    print(f' INPUT: size: {len(data)} compressed size: {len(data_z)}')

    output = bytearray()
    #for b in ck1.key.to_bytes(DOMAIN, 'big'):
    #     output.append(b)
    #for b in ck2.key.to_bytes(DOMAIN, 'big'):
    #    output.append(b)
    for b in ck1.residual:
        output.append(b)
    for b in ck2.residual:
        output.append(b)

    output_z = zlib.compress(output, 9)
    print(f' OUTPUT: size: {len(output)} compressed size: {len(output_z)}')
    
    with open("input.dat", "wb") as binary_file:
        binary_file.write(data)

    with open('output.dat', 'wb') as binary_file:
        binary_file.write(output)
