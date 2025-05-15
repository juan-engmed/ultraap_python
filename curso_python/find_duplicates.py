def find_duplicates(lst):
    counts = {}
    duplicates = set()

    for item in lst:
        if item in counts:
            counts[item] += 1
            if counts[item] == 2:  # adiciona só na 2ª ocorrência
                duplicates.add(item)
        else:
            counts[item] = 1

    return duplicates

def main():
    list_a = []
    
    while True:
        user_input = input('Digite o valor para adicionar a lista, ou skip para obter os items duplicados e finalizar')
        
        if user_input == 'skip':
            break
        
        list_a.append(user_input)
    
    print(find_duplicates(list_a))
    
    print('Programa Finalizado')
    
if __name__ == "__main__":
    main()