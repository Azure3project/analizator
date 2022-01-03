prime = 257
mod = [10**9 + 7, 998244353]
powers = []
products = []
products_hash = []


def init_hash():
    global powers
    powers = [[1] for _ in range(len(mod))]
    for m in range(len(mod)):
        for i in range(1000):
            powers[m].append((powers[m][-1] * prime) % mod[m])

def compute_hash_table(txt):
    result = [[] for _ in range(len(mod))]
    for i in range(len(mod)):
        for c in txt:
            if len(result[i]) == 0:
                result[i].append(ord(c))
            else:
                result[i].append(((result[i][-1] * prime) % mod[i]) + ord(c) % mod[i])
    return result

def compute_hash(txt):
    result = []
    for m in range(len(mod)):
        for c in txt:
            if len(result) == m:
                result.append(ord(c))
            else:
                result[-1] *= prime
                result[-1] += ord(c)
                result[-1] %= mod[m]
    return result

def extract_hash(text_hash, l, r):
    if l > 0:
        res = [0, 0]
        for i in range(len(mod)):
            res[i] = ((text_hash[i][r] - (text_hash[i][l - 1] * powers[i][r - l + 1]) % mod[i]) + mod[i]) % mod[i]
    else:
        res = [text_hash[0][r], text_hash[1][r]]
    return res

def compare_hash(hash1, hash2):
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            return False
    return True

def preprocess(tmp):
    subs = {'ą' : 'a', 'ę' : 'e', 'ś' : 's', 'ć' : 'c', 'ź' : 'z', 'ż' : 'z', 'ó' : 'o', 'ń' : 'n', 'ł' : 'l'}
    tmp = list(tmp.lower())
    tmp = [c if c not in subs else subs[c] for c in tmp]
    return ''.join(tmp)

def read_list():
    global products, products_hash
    with open('produkty.list', encoding = 'utf-8') as file:
        for line in file:
            products.append(preprocess(line.rstrip()))
    products = list(dict.fromkeys(products))
    products.sort(key = len, reverse = True)
    products_hash = [compute_hash(product) for product in products]

def init_extracting():
    init_hash()
    read_list()

def extract_products(text):
    text = preprocess(text.lower())
    text_hash = compute_hash_table(text)
    found = [False for _ in text]
    products_found = []
    for product, hash in zip(products, products_hash):
        pos = 0
        while pos + len(product) <= len(text):
            if found[pos] == False and compare_hash(extract_hash(text_hash, pos, pos + len(product) - 1), hash):
                products_found.append(product)
                print(f'I found {product} on the list')
                for i in range(pos, pos + len(product)):
                    found[i] = True
                pos += len(product) - 1
            pos += 1
    return products_found
