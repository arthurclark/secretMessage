secret_language = {
    'a' : '-`!`',
    'b' : '&@^#',
    'c' : '?*)%',
    'd' : '#@(!',
    'e' : '}*@^',
    'f' : '+#*@',
    'g' : '#(@)',
    'h' : '\|<>',
    'i' : '+!)$',
    'j' : '-_>!',
    'k' : ')#*(',
    'l' : ')$*&',
    'm' : '*!^$',
    'n' : '*#)%',
    'o' : '#*&^',
    'p' : '+|?!',
    'q' : '%*^&',
    'r' : '#$%^',
    's' : '^#*)',
    't' : '*^#(',
    'u' : '||++',
    'v' : '??@#',
    'w' : '$$&(',
    'x' : '||}{',
    'y' : '__-@',
    'z' : '(#)$',
    ' ' : '_#*)'
}
print("Would you like to encode or decode a message? (1 for encode, 2 for decode)")
eord = input()

if (eord == "1"):
    print("Enter the message you would like to encode:")
    response = input()
    encoded_text = ""
    response = response.lower()
    for i in response:
        encoded_text += secret_language[i]
    print("Below is the encoded text: ")
    print(encoded_text)

else:
    print("Enter a message to be decoded:")
    to_be_decoded = input()
    letter_blocks = [to_be_decoded[i:i+4] for i in range(0, len(to_be_decoded), 4)]
    actual_letters = list(secret_language.keys())
    letter_definitons = list(secret_language.values())
    final_string = ""
    for i in letter_blocks:
        position = letter_definitons.index(i)
        final_string += actual_letters[position]
    print("Below is the decoded text: ")
    print(final_string)
