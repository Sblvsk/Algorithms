import hashlib


def substring_count(s):
    x = str(s).lower()
    length = len(x)
    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(x[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


some_string = 'beer boop'

print(f'Количество подстрок в строке {some_string}: {substring_count(some_string)}')