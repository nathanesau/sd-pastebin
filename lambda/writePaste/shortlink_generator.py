from hashlib import md5

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_character(digit):
    return BASE62[digit]

def base_encode(num, base=62):
    digits = []
    while num > 0:
        remainder = num % base
        digits.append(remainder)
        num = num // base
    digits = digits[::-1]
    return list(map(get_character, digits))

def generate_url(request_id, timestamp, url_length=7):
    key = str(request_id + timestamp).encode('utf-8')
    hexvalue = md5(key).hexdigest()
    decvalue = int(hexvalue, 16)
    url = base_encode(decvalue)
    return ''.join(url[:7])