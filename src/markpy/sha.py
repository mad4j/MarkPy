
import itertools
import hashlib

if __name__ == '__main__':

    #caratteri = '~\'\\|!"$%&/()}{=?^+*@#[]-_.,;:<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    caratteri = 'abcdefghijklmnopqrstuvwxyz'
    it = itertools.product(caratteri, repeat=7)

    #print((int.from_bytes(hashlib.sha256(b"[k!a").digest())+43) % 10**10)
    #print((int.from_bytes(hashlib.sha256(b"!]xWh").digest())-3) % 10**10)
    #print((int.from_bytes(hashlib.sha256(b"&A:an").digest())-10) % 10**10)
    #print((int.from_bytes(hashlib.sha256(b"=SHAT").digest())+63) % 10**10)
    #print(int.from_bytes(hashlib.sha256(b"#im*E").digest()) % 10**10)

    for x in it:
        x = "".join(x)
        h = hashlib.sha512(bytes(x, "UTF-8")).digest()
        d = (int.from_bytes(h) % 10**10) - 3332149721
        if abs(d) < 10:
            print(f"{x}: {d}")