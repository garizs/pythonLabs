text = 'Rela aleR joker joker rekoj Rela aleR joker rekoj'
first_word = ''
second_word = ''
correct_letters = 0
for first_word_index in range(len(text)):
    if not ord(text[first_word_index]) == 32:
        first_word += text[first_word_index]
    else:
        for second_word_index in range(first_word_index + 1, len(text)):
            if not ord(text[second_word_index]) == 32:
                second_word += text[second_word_index]
            if second_word_index == len(text) - 1 or ord(text[second_word_index]) == 32:
                if len(first_word) == len(second_word):
                    index = len(second_word) - 1
                    correct_letters = 0
                    for correct_letters_index in range(len(first_word)):
                        if first_word[correct_letters_index] == second_word[index]:
                            correct_letters += 1
                            index -= 1
                        else:
                            break
                else:
                    second_word = ''
                    continue
                if correct_letters == len(first_word):
                    print(first_word, second_word, end='\n')
                second_word = ''
                continue
        first_word = second_word = ''
