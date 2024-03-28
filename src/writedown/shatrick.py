
import os
import binascii
import hashlib
import zlib
from functools import wraps
from time import time


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

def zeros(bytes):
    value = 0
    for b in bytes:
        value += b.bit_count()
    return 8*len(bytes) - value


if __name__ == '__main__':
    data = os.urandom(32)
    print(f'Input data: {binascii.hexlify(bytearray(data))}')
    print(f'zeros: {zeros(data)}')

    target = zeros(data)

    domain = 3
    max = target
    result = data
    head = 0
    for v in range(1 << 8*domain):

        h = hashlib.sha256(v.to_bytes(domain, 'big')).digest()
        t = bytes(a ^ b for (a, b) in zip(data, h))

        r = zeros(t)
        if r > max:
            print(f'value: {v:010x}, zeros: {r} result: {binascii.hexlify(bytearray(t))}')
            max = r
            result = t
            head = v

        if v % 0x1000000 == 0:
            print(f'{v:010x}: max: {max}')

    print(f'RESULT: value: {head:010x}, zeros: {max} result: {binascii.hexlify(bytearray(result))}')

    data_z = zlib.compress(data, 9)
    result_z = zlib.compress(result, 9)
    print(f'compressed size: data: {len(data_z)}, result: {len(result_z)}')

    with open("input.dat", "wb") as binary_file:
        binary_file.write(data)

    with open('output.dat', 'wb') as binary_file:
        binary_file.write(head.to_bytes(domain, 'big'))
        binary_file.write(result)
