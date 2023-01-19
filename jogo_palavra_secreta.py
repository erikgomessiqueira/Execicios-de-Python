import os
secret_word = 'banana'
len_secret_word = len(secret_word)
correct_word ='*'*len_secret_word
attempts_counted = 0

while True:
        typed_word = input('Digite uma letra: ').lower()
        try:
            len_typed_word = len(typed_word)
            if len_typed_word>1 or len_typed_word <1: print(correct_word); continue

            new_word=''

            for index in range(len_secret_word):
                if typed_word == secret_word[index].lower():
                    new_word+=secret_word[index]
                elif correct_word[index] == '*':
                    new_word += '*'
                else:
                    new_word+=correct_word[index]

            correct_word = new_word.capitalize()
            os.system('clear')
            print(f'Palavra: {correct_word}')

            attempts_counted+=1

            if correct_word.capitalize() == secret_word.capitalize():
                os.system('clear')
                print(f'Você acertou a palavra!!!'.upper())
                print(f'Palavra: {correct_word}')
                print(f'Tentativas: {attempts_counted}'.capitalize())
                break
        except:
            print(f'Palavra: {correct_word}')