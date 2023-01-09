import win32com.client
def encrypt(key,content): # key:密钥,content:明文
    EncryptedData = win32com.client.Dispatch('CAPICOM.EncryptedData')
    EncryptedData.Algorithm.KeyLength = 5
    EncryptedData.Algorithm.Name = 2
    EncryptedData.SetSecret(key)
    EncryptedData.COntent= content
    return EncryptedData.Encrypt()
def decrypt(key,content): # key:密钥,content:密文
    EncryptedData = win32com.client.Dispatch('CAPICOM.EncryptedData')
    EncryptedData.Algorithm.KeyLength = 5
    EncryptedData.Algorithm.Name = 2
    EncryptedData.SetSecret(key)
    EncryptedData.Decrypt(content)
    str = EncryptedData.Content
    return str
key = "tron"
centosUserRoot = encrypt(key, 'root pp')
centosUser1 = encrypt(key, 'tron 1257212188.a')
centosUser2 = encrypt(key, 'anti antianti')
s2 = decrypt(key, centosUserRoot)
print(centosUserRoot,s2)

# MGEGCSsGAQQBgjdYA6BUMFIGCisGAQQBgjdYAwGgRDBCAgMCAAECAmYBAgFABAgq
# GpllWj9cswQQh/fnBUZ6ijwKDTH9DLZmBgQYmfaZ3VFyS/lq391oDtjlcRFGnXpx
# lG7o
# hello world