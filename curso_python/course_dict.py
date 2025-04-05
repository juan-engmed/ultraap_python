def test_dict_pessoa():
    pessoa = {'nome': 'Juan', 'idade': 33, 'cidade': 'Rio de Janeiro'}
    print(pessoa)
    pessoa.update({'idade': 34, 'cidade': 'Porto'})
    print(pessoa)

    pessoa['profissao'] = 'Engenheiro'
    print(pessoa)

    #Apagar com segurança (sem erro) e também retorna o valor apagado, caso necessite do mesmo
    pessoa.pop('cidade', None)
    print(pessoa)

    # dados = {'a': 1, 'b': 2, 'c': 3}
    # ultimo = dados.popitem()
    # print(ultimo)  # ('c', 3)
    # print(dados)   # {'a': 1, 'b': 2}
    
def dict_1_to_5_square():
    numbers_square = {}
    for i in range(1,6):
        numbers_square.update({f'{i}': i*i})
    
    #List Comprehension
    #numbers_square = {x: x**2 for x in range(1, 6)}
    
    print(numbers_square)

def verify_key_in_dict(key):
    test_dict = {'nome', 'rg', 'cpf'}
    if key in test_dict:
        print('a key está no dict')
    else:
        print('key não está no dict')

def frequency_word_in_phrase(phrase):
    contagem_palavras = {}
    palavras = phrase.split()
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    print(contagem_palavras)

def main():
    test_dict_pessoa()
    dict_1_to_5_square()
    verify_key_in_dict('not')

    phrase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
    frequency_word_in_phrase(phrase)


#frase = "oi tudo bem"
#frase.split()  # resultado: ['oi', 'tudo', 'bem']

if __name__ == "__main__":
    main()