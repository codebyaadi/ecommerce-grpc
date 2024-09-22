import base64
import codecs
import sys

# Function to encrypt the text
def encrypt(text: str) -> str:
    # ROT13 encryption
    rot13_encrypted = codecs.encode(text, "rot13")

    # Base64 encode
    base64_encoded = base64.b64decode(rot13_encrypted.encode()).decode()

    print("Encrypted Text:", base64_encoded)

# Function to decrypt the input
def decrypt(encoded_text: str) -> str:
    # Base64 decoding
    base64_decoded = base64.b64decode(encoded_text).decode()
    
    # ROT13 decryption
    rot13_decrypted = codecs.decode(base64_decoded, 'rot_13')
    
    print("Decrypted Text:", rot13_decrypted)

# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print("Usage: python encrypt_decrypt.py [encrypt|decrypt] [text]")
    sys.exit(1)

# Based on the argument, call the appropriate function
if sys.argv[1] == "encrypt":
    encrypt(sys.argv[2])
elif sys.argv[1] == "decrypt":
    decrypt(sys.argv[2])
else:
    print("Invalid option:", sys.argv[1])
    print("Use 'encrypt' or 'decrypt'")
    sys.exit(1)