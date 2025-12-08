def extract_vowels(input_string):
    vowels = "aeiouAEIOU"
    extracted_vowels = [char for char in input_string if char in vowels]
    return ''.join(extracted_vowels)
