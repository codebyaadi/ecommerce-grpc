#!/bin/bash

# Function to encrypt the input
encrypt() {
    local input="$1"

    # ROT13 Encryption
    encrypted=$(echo "$input" | tr 'A-Za-z' 'N-ZA-Mn-za-m')

    # Base64 Encode
    encoded=$(echo "$encrypted" | base64)
    
    echo "Encrypted text: $encoded"
}

# Function to decrypt the input
decrypt() {
    local input="$1"
    
    # Base64 decoding
    decoded=$(echo "$input" | base64 --decode)
    
    # ROT13 decryption
    decrypted=$(echo "$decoded" | tr 'A-Za-z' 'N-ZA-Mn-za-m')
    
    echo "Decrypted Text: $decrypted"
}

# Check if the number of arguments is correct
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 [encrypt|decrypt] [text]"
    exit 1
fi

# Based on the argument, call the appropriate function
if [ "$1" == "encrypt" ]; then
    encrypt "$2"
elif [ "$1" == "decrypt" ]; then
    decrypt "$2"
else
    echo "Invalid option: $1"
    echo "Use 'encrypt' or 'decrypt'"
    exit 1
fi
