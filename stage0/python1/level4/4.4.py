import hashlib

s = input("enter string : ")

md5_hash = hashlib.md5()
md5_hash.update(s.encode('utf-8'))
print( md5_hash.hexdigest())

