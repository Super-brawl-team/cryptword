# 🔐 CWS File Encryptor

A simple **RC4-based file encryptor/decryptor** with support for per-file and batch folder processing.
Includes **CWS v2 format** with magic bytes, versioning, and password verification.

## ✨ Features

- 🔑 Generate or provide your own encryption key
- 📂 Encrypt/decrypt single files or entire folders
- 🧩 Preserves file extensions
- ⚡ Uses lightweight [RC4](https://en.wikipedia.org/wiki/RC4) stream cipher
- 🛡️ Includes password verification to prevent wrong-key corruption

## 📖 Usage

**1. Run the script**
`python main.py`

**2. Choose action**
Encrypt or decrypt (e/d) >>

**3. Provide a key**

**Encrypting:** Press enter to auto-generate a secure key

**Decrypting:** Enter the exact key used during encryption

**4. Select scope**
Apply to all files in folder? (y/n) >>

**5. (If not all files) Choose a filename**
File name >> example.png

## 📂 File Format (CWS v2)

Each encrypted file follows this structure:

[ magic bytes   ]  8 bytes   → b"\x69\x74crypt"  
[ file ext      ]  string  
[ version       ]  vint      → currently 2  
[ password check]  bytes     → encrypted "cws"  
[ file data     ]  encrypted payload

## ⚠️ Notes

Files encrypted with **CWS v1 (*SUCCESS* header) are not supported** in this version.

Keep your key safe — without it, files **cannot** be decrypted.

Recommended for **personal/educational** use, not production-grade security.

## 🚀 Example

Encrypt all files in a folder:
```
python main.py
Encrypt or decrypt (e/d) >> e
Set the key string here (press return to generate a random one) >> 
The randomly generated key is :3g7hJQK2LmXc9yT4F6vD0BZnSpR1aEWsXoYtU5Hb , make sure to keep it
Apply to all files in folder? (y/n) >> y
```

Decrypt a single file:
```
python main.py
Encrypt or decrypt (e/d) >> d
Set the key string here >> 3g7hJQK2LmXc9yT4F6vD0BZnSpR1aEWsXoYtU5Hb
Apply to all files in folder? (y/n) >> n
File name >> secret.cws
```
##
💡 Tip: Store your key in a password manager to avoid losing access.
##
