# Dadas duas strings s e t, escreva uma função que determine se t é um anagrama válido de s
# s = "listen"
# t = "silent"
# True

# s = "rat"
# t = "car"
# False

def normalize_input(text):
    if not isinstance(text, str):
        raise ValueError(f'Valor [{text}] inválido | É esperado String')
    return text.lower().replace(" ", "")

def ensure_same_length(first_word, second_word):
    if len(first_word) != len(second_word):
        raise ValueError('As palavras fornecidas têm tamanhos diferentes e, por isso, não podem ser anagramas.')
    
def get_alphabet_index(letter):
    return ord(letter) - ord('a') #Tabela ASCII A = 65, B = 66, C = 67

def is_anagram(first_word, second_word):
    letter_balance = [0] * 26 # [0,0,0,0,0,0,0,0,0...0] | Temos um valor para cada letra | Baba = [2,2,0,0,0,0....]

    for index in range(len(first_word)):
        letter_from_first_word = first_word[index]
        letter_from_second_word = second_word[index]

        letter_balance[get_alphabet_index(letter_from_first_word)] += 1
        letter_balance[get_alphabet_index(letter_from_second_word)] -= 1

    for value in letter_balance:
        if value != 0:
            return False
    
    return True

    # for letter in first_word:
    #     index = return_index_from_letter_balance(letter)
    #     letter_balance[index] += 1 # EX: letra A = [1,0,0,0,0...]
    
    # for letter in second_word:
    #     index = return_index_from_letter_balance(letter)
    #     letter_balance[index] -= 1

    # for balance in letter_balance:
    #     if balance != 0:
    #         return False
    #     return True

def main():
    try:
        first_word = 'listen'
        second_word = 'silent'
        normalize_input(first_word)
        normalize_input(second_word)

        ensure_same_length(first_word, second_word)

        result = is_anagram(first_word,second_word)
        print(f'Is anagram = {result}')

    except ValueError as ve_ex:
        print(f'[Input Inválido] {ve_ex}')
    except Exception as ex:
        print(f'[Erro inesperado] {ex}')

if __name__ == "__main__":
    main()