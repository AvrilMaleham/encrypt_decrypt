def encrypt_decrypt(text, mode, key=None):
    special_chars = {" ": "01", ",": "03", ".": "05", "\n": "07", "'": "09"}
    marker = "13579"
    
    # Enforce key limits: Key must be an even number between 10 and 40
    if key is not None and (key % 2 != 0 or key < 10 or key > 40):
        raise ValueError("Key must be an even number between 10 and 40.")
    
    if mode == "encode":
        encoded_text = []
        for char in text.upper():  # Ensure case insensitivity
            if char.isalpha():
                # Encode using the key
                encoded_number = str(key + (ord(char) - ord('A')) * 2)
                encoded_text.append(encoded_number)
            elif char in special_chars:
                encoded_text.append(special_chars[char])
            else:
                encoded_text.append(char)
        return "".join(encoded_text) + marker + str(key)
    
    elif mode == "decode":
        if marker not in text:
            raise ValueError("Invalid encoded text format.")
        key_index = text.index(marker) + len(marker)
        key_str = text[key_index:]
        
        try:
            key = int(key_str)
        except ValueError:
            raise ValueError("Invalid key format in encoded text.")
        
        encoded_numbers = text[:key_index - len(marker)]
        decoded_text = []
        
        # Create a temporary mapping for decoding
        decoding_map = {str(key + (i * 2)): chr(ord('A') + i) for i in range(26)}
        decoding_map.update({v: k for k, v in special_chars.items()})
        
        i = 0
        while i < len(encoded_numbers):
            for length in range(2, 0, -1):  # Numbers are always 2 digits long
                num = encoded_numbers[i:i + length]
                if num in decoding_map:
                    decoded_text.append(decoding_map[num])
                    i += length
                    break
            else:
                i += 1  # Move to the next character if no match found
        
        return "".join(decoded_text)
    else:
        raise ValueError("Mode must be 'encode' or 'decode'.")

# Example usage for encoding and decoding
if __name__ == "__main__":
    mode = input("Enter mode (encode/decode): ").strip().lower()
    text = input("Enter text: ").strip()
    
    if mode == "encode":
        key = int(input("Enter key (even number between 10 and 40): ").strip())
        try:
            print("Encoded Text:", encrypt_decrypt(text, mode, key))
        except ValueError as e:
            print("Error:", e)
    elif mode == "decode":
        try:
            print("Decoded Text:", encrypt_decrypt(text, mode))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid mode entered. Please choose 'encode' or 'decode'.")
