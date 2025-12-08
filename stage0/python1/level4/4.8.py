def xor_encrypt(input_string, key):
    output = []
    for i in range(len(input_string)):
        current_char = input_string[i]
        current_key = key[i % len(key)]
        encrypted_char = chr(ord(current_char) ^ ord(current_key))
        output.append(encrypted_char)
    return ''.join(output)


