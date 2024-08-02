# Dictionary for encoding
encoding_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
}

print("Welcome to 'Text to Morse Code' converter.")

input_text = input("Please type the text you want to convert to Morse Code: ")

# Encoding
converted_message = ""
symbols_present = False
for character in range(0, len(input_text)):
    # Get needed letter from input
    letter = input_text[character]
    letter = letter.upper()
    try:
        converted_letter = encoding_dict[letter]
    except KeyError:
        # In case of an unknown character, do not convert it
        if letter == ' ':
            converted_letter = ' '
        else:
            converted_letter = letter
            # Detection for symbols in input
            symbols_present = True
    finally:
        converted_message += converted_letter
        converted_message += ' '

# User output
print("Your text in Morse Code: ")
print(converted_message)
print("In between every letter there's a gap. In place of a gap from original message there's two gaps.")
if symbols_present:
    print("Symbols are not convertable to Morse Code. They were not translated.")
