import string

def napoleon_code(text, move_num=0):
    result_list = []
    end_of_while = True
    alphovite = string.ascii_lowercase
    for letter in text:
        letter = letter.lower()
        if letter in alphovite:
            letter_index = alphovite.index(letter)

            while end_of_while:
                try:
                    end_of_while = False
                    result_list.insert(0, alphovite[abs(letter_index + move_num)])
                except:
                    move_num -= len(alphovite)
                    end_of_while = True
            end_of_while = True
        else:
            print(letter, end='')
    result_list.reverse()
    print(result_list)

napoleon_code('hallo', 30)

print('end')