# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true

def normalize_input(input_text):
    if not isinstance(input_text, str):
        raise ValueError(f'{input_text} não é do tipo esperado String')
    return input_text.lower().replace(" ","")

def get_alphabet_balance_index(letter):
    return ord(letter) - ord('a')

#Solution 1
def is_pangram(text):
    
    alphabet_balance = [0] * 26

    for letter in text:
        index = get_alphabet_balance_index(letter)
        alphabet_balance[index] += 1
    
    for balance in alphabet_balance:
        if balance == 0:
            return False
    return True

#Solution 2
# def is_pangram(text):

#     alphabet_set = set()

#     alphabet_balance = [0] * 26

#     for letter in text:
#         alphabet_set.add(letter)
#         # index = get_alphabet_balance_index(letter)
#         # alphabet_balance[index] += 1
    
#     if len(alphabet_set) == 26:
#         return True
#     return False

def main():
    try:
        text = 'thequickbrownfoxjumpsoverthelazydog'
        text_normalized = normalize_input(text)

        result =  is_pangram(text_normalized)
        if result:
            print(f'{text_normalized} é Pangram')
        else:
            print(f'{text_normalized} NÃO é pangram')

    except Exception as ex:
        print(f'Ocorreu um erro: {ex}')

if __name__ == "__main__":
    main()