import random
import string
import struct
from Cryptography.rc4 import CryptoRc4

key = input("Set the key string here (press return to generate a random one) >> ").strip()
if not key:
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
    print("The randomly generated key is :" + key + " , make sure to keep it")

request = input("Encrypt or decrypt (e/d) >> ").strip().lower()
file = input("File name >> ").strip()

crypto = CryptoRc4(key)

def encrypt():
    with open(file, "rb") as original:
        file_data = original.read()
    
    file_ext = file.split('.')[-1]
    file_ext_bytes = file_ext.encode('utf-8') 
    ext_length = len(file_ext_bytes)  # avoiding using bs bytestream :skull:

    header = b"SUCCESS" + struct.pack("I", ext_length) + file_ext_bytes

    encrypted_data = crypto.encrypt(header + file_data)

    output_file = file.replace("." + file_ext, "") + ".cws"

    with open(output_file, "wb") as encrypted_file:
    
        encrypted_file.write(encrypted_data)

    print(f"Encrypted file saved as: {output_file}")

def decrypt():
    with open(file, "rb") as encrypted_file:
        file_data = encrypted_file.read()
    decrypted_data = crypto.decrypt(file_data)
    if decrypted_data.startswith(b""):
        print("[ERROR] This file has been encrypted with csw2, please use the appropriate version decryptor")
    if not decrypted_data.startswith(b"SUCCESS"):
        print("[ERROR] Incorrect decryption password!")
        return
    
    decrypted_data = decrypted_data[7:]
    ext_length = struct.unpack("I", decrypted_data[:4])[0]
    decrypted_data = decrypted_data[4:]

    file_ext = decrypted_data[:ext_length].decode('utf-8')
    decrypted_data = decrypted_data[ext_length:] # Do NOT critizise i broke my head to make that :sob:

    

    output_file = file.replace(".cws", f".{file_ext}")
    with open(output_file, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Decrypted file saved as: {output_file}")

if request == "e":
    encrypt()
elif request == "d":
    decrypt()
else:
    print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")