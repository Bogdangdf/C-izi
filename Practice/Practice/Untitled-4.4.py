from Crypto.Hash import SHA256
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Util.Padding import pad, unpad

message = b"Hello world"

hash_obj = SHA256.new(message)
hash_value = hash_obj.hexdigest()
print(hash_value)

key = get_random_bytes(16)
cipher_aes = AES.new(key, AES.MODE_CBC)
ciphertext = cipher_aes.encrypt(pad(message, AES.block_size))
iv = cipher_aes.iv

cipher_aes_dec = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher_aes_dec.decrypt(ciphertext), AES.block_size)
print(decrypted)

rsa_key = RSA.generate(2048)
private_key = rsa_key
public_key = rsa_key.publickey()

sign_hash = SHA256.new(message)
signature = pkcs1_15.new(private_key).sign(sign_hash)

pkcs1_15.new(public_key).verify(sign_hash, signature)
print("signature valid")
