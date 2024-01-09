import string

def napoleon_code(text, move_num=0):
    result_list = []
    alphovite = string.ascii_lowercase
    for letter in text:
        letter = letter.lower()
        if letter in alphovite:
            letter_index = alphovite.index(letter)
            result_list.append(alphovite[abs(letter_index + (move_num % len(alphovite)))])
        else:
            print(letter, end='')
    print(''.join(result_list))
    print(len(alphovite))

napoleon_code('hallo', 82)

print('end')
