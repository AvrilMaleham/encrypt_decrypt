def encrypt_decrypt(text, mode, key=None):
    special_chars = {" ": "01", ",": "03", ".": "05", "\n": "07", "'": "09"}
    marker = "13579"
    
    if mode == "encode":
        if key is None or key % 2 != 0:
            raise ValueError("Key must be an even number for encoding.")
        encoded_text = []
        for char in text.upper():  # Ensure case insensitivity
            if char.isalpha():
                encoded_text.append(str(key + (ord(char) - ord('A')) * 2))
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
            for length in range(3, 0, -1):  # Numbers can be 1-3 digits long
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

""" if __name__ == "__main__":
    # Predefined test values instead of input()
    test_cases = [
        {"mode": "encode", "text": "can you find out my secret", "key": 2},
        {"mode": "decode", "text": "622801503042011218288013042400126500138106361040135792"}
    ]
    
    for case in test_cases:
        try:
            if case["mode"] == "encode":
                print("Encoded Text:", encrypt_decrypt(case["text"], case["mode"], case["key"]))
            elif case["mode"] == "decode":
                print("Decoded Text:", encrypt_decrypt(case["text"], case["mode"]))
        except ValueError as e:
            print("Error:", e) """

if __name__ == "__main__":
    mode = input("Enter mode (encode/decode): ").strip().lower()
    text = input("Enter text: ").strip()
    
    if mode == "encode":
        key = int(input("Enter key (even number): ").strip())
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