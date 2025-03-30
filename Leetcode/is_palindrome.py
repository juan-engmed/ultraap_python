
def normalize_input(text):
    if not isinstance(text, str):
        raise ValueError(f'{text} inválido, esperado String')
    return text.lower().replace(" ","")

def is_palindrome(text):

    for i in range(len(text)//2):
        letter_a = text[i]
        letter_b = text[(len(text) - 1) -i]
        if letter_a != letter_b:
            return False
    return True


def main():
    try:
        phrase_to_verify = 'mirim'

        phrase_to_verify_normalized = normalize_input(phrase_to_verify)

        if is_palindrome(phrase_to_verify_normalized):
            print(f'A frase {phrase_to_verify} é palíndrome')
        else:
            print(f'A frase {phrase_to_verify} Não é palíndrome')
    except ValueError as vex:
        print(f'Erro: {vex}')
    except Exception as ex:
        print(f'Erro: {ex}')

if __name__ == "__main__":
    main()