
import os
import binascii
import hashlib

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
    
    domain = 5
    max = target
    for v in range(1 << 8*domain):
        
        h = hashlib.sha256(v.to_bytes(domain, 'big')).digest()
        t = bytes(a ^ b for (a, b) in zip(data, h))
        
        r = zeros(t)
        if r > max:
            print(f'value: {v:x}, zeros: {r} result: {binascii.hexlify(bytearray(t))}')
            max = r
            