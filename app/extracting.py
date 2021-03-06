from cmath import inf
from app.categories import Bread
from app.categories import Other_grain_products
from app.categories import Sauces
from app.categories import Diary
from app.categories import Meat_fish_eggs
from app.categories import Vegetables
from app.categories import Fruits
from app.categories import Fats
from app.categories import Sugar_and_snacks
from app.categories import Water_and_drinks
from app.categories import Ready_meals
from app.categories import Frozen_foods
from app.categories import Dry_foods
from app.categories import Cigarettes
from app.categories import Toothpaste
from app.categories import Other_products

from datetime import date, timedelta

prime = 257
mod = [10 ** 9 + 7, 998244353]
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
    subs = {'??': 'a', '??': 'e', '??': 's', '??': 'c', '??': 'z', '??': 'z', '??': 'o', '??': 'n', '??': 'l'}
    tmp = list(tmp.lower())
    tmp = [c if c not in subs else subs[c] for c in tmp]
    return ''.join(tmp)


def read_list():
    global products, products_hash
    with open('app/produkty.list', encoding='utf-8') as file:
        for line in file:
            products.append(preprocess(line.rstrip()))
    products = list(dict.fromkeys(products))
    products.sort(key=len, reverse=True)
    products_hash = [compute_hash(product) for product in products]


def init_extracting():
    init_hash()
    read_list()


def extract_products(text):
    text = preprocess(text.lower())
    text_hash = compute_hash_table(text)
    found = [False for _ in text]
    products_found = []
    dates = []
    for product, hash in zip(products, products_hash):
        pos = 0
        while pos + len(product) <= len(text):
            if found[pos] == False and compare_hash(extract_hash(text_hash, pos, pos + len(product) - 1), hash):
                if product in products_found:
                    for i in range(pos, pos + len(product)):
                        found[i] = True
                    pos += len(product) - 1
                    pos += 1
                    continue

                products_found.append(product)

                days = 0
                current_date = date.today()
                
                while days == 0:
                    for i in Bread:
                        if i == product:
                            days = 2
                    for i in Other_grain_products:
                        if i == product:
                            days = 365       
                    for i in Sauces:
                        if i == product:
                            days = 365                
                    for i in Diary:
                        if i == product:
                            days = 14
                    for i in Meat_fish_eggs:
                        if i == product:
                            days = 183
                    for i in Vegetables:
                        if i == product:
                            days = 14
                    for i in Fruits:
                        if i == product:
                            days = 14
                    for i in Fats:
                        if i == product:
                            days = 365 
                    for i in Sugar_and_snacks:
                        if i == product:
                            days = 365
                    for i in Water_and_drinks:
                        if i == product:
                            days = 365
                    for i in Ready_meals:
                        if i == product:
                            days = 7
                    for i in Frozen_foods:
                        if i == product:
                            days = 365
                    for i in Dry_foods:
                        if i == product:
                            days = inf
                    for i in Cigarettes:
                        if i == product:
                            days = 365
                    for i in Toothpaste:
                        if i == product:
                            days = 730
                    for i in Other_products:
                        if i == product:
                            days = inf
                    #days = inf
                
                if days == -1:
                    print(f'I found {product} on the list. I could not establish its expiration date.')
                    dates.append(0)
                elif days == inf:
                    print(f'I found {product} on the list. It does not expire.')
                    dates.append(0)
                else:
                    expiration_date = current_date + timedelta(days)
                    print(f'I found {product} on the list. Its expiration date is {expiration_date}.')
                    dates.append(expiration_date)
                
                for i in range(pos, pos + len(product)):
                    found[i] = True
                pos += len(product) - 1
            pos += 1
    print(products_found)
    print(dates)
    return products_found, dates
