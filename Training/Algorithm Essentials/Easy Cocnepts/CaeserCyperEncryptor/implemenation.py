def caeserCipherEncryptor(string, key):
    key = key % 26
    res = ''
    for character in string:
        lc = ord(character) + key
        if lc <= 122:
            res = res + chr(lc)
        else:
            res = res + chr(96+(lc % 122))
    return res

if __name__ == '__main__':
    print(caeserCipherEncryptor("xyz", 2))

