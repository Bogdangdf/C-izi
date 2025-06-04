def analyze_string (S):

    vowels = "aeiouAEIOU"
    voweletter = ""
    consonant_let = ""

    for char in S:
        if char.isalpha():
            if char in vowels:
                voweletter += char 
            else:
                consonant_let += char

    return (voweletter, len(voweletter), consonant_let)

input_str = "abcdefg"
result = analyze_string(input_str)
print(result)