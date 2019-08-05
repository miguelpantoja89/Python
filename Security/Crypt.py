from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher_suit = Fernet(key)

cipher_text = cipher_suit.encrypt(b'Text will be encrypted') #we need byte format 

print (cipher_text)

original = cipher_suit.decrypt(cipher_text)

print (original)