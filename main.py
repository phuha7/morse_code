# creating a mapping for each character to their corresponding morse code
dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '!': '-.-.--',
    ' ': '/'
}


def translate():
    string_to_convert = input("Enter the string you want to convert to morse code: ")

    converted_string = ''

    try:
        for letter in string_to_convert:
            converted_string += dict[letter]
            converted_string += ' '
    except KeyError as e:
        print(str(e) + ' cannot be translated.')

    print(converted_string)


on = True


while on:
    translate()
    ans = input("Enter 'n' to exit or Enter to continue: ").lower()

    if ans == 'n':
        on = False


