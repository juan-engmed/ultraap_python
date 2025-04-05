def test_dict_pessoa():
    pessoa = {'nome': 'Juan', 'idade': 33, 'cidade': 'Rio de Janeiro'}
    print(pessoa)
    pessoa.update({'idade': 34, 'cidade': 'Porto'})
    print(pessoa)

    pessoa.update({'profissão': 'Engenheiro de Telecomunicações'})
    print(pessoa)

    pessoa.pop('idade')
    print(pessoa)
    
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

def main():
    test_dict_pessoa()
    dict_1_to_5_square()
    verify_key_in_dict('not')





if __name__ == "__main__":
    main()