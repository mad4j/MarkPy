
import itertools
import hashlib
import multiprocessing
from typing import Tuple
from joblib import Parallel, delayed

def task(item: str, threshold: int = 10) -> None | Tuple[int, str]:
    value = bytes(item, "UTF-8")
    for i in range(100):
        value = hashlib.sha256(value).digest()
        delta = (int.from_bytes(value) % 10**10) - 3332149721
        if abs(delta) < threshold:
             #print(f"{i+1}:{item}: {delta}")
            return (i, item)
        else:
            return None


if __name__ == '__main__':
    
    #CHARSET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    #CHARSET = 'abcdefghijklmnopqrstuvwxyz'
    CHARSET = 'Ω℧♀♂♠♡♢♣♤♥♦♧♩♪♫♬©±µ¶ΓΔΙΞΛΣΦΨαβγδεθλ~\'\\|!"$%&/()}{=?^+*@#[]-_.,;:<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789àèéìòù§ç€£'

    num_cores = multiprocessing.cpu_count()
    print(f'using {num_cores} cores...')

    it = itertools.product(CHARSET, repeat=3)

    results = Parallel(n_jobs=num_cores)(delayed(task)(item) for item in it)

    #print((int.from_bytes(hashlib.sha256(b"[k!a").digest())+43) % 10**10)
    #print((int.from_bytes(hashlib.sha256(b"!]xWh").digest())-3) % 10**10)
    #print((int.from_bytes(hashlib.sha256(b"&A:an").digest())-10) % 10**10)
    #print((int.from_bytes(hashlib.sha256(b"=SHAT").digest())+63) % 10**10)
    #print(int.from_bytes(hashlib.sha256(b"#im*E").digest()) % 10**10)

    

    #for x in it:
    #    task("".join(x), 1000)
        #    x = "".join(x)
        #    h = bytes(x, "UTF-8")
        #    for i in range(100):
        #        h = hashlib.sha256(h).digest()
        #        d = (int.from_bytes(h) % 10**10) - 3332149721
        #        if abs(d) < 10:
        #            print(f"{i+1}:{x}: {d}")
