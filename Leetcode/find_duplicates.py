def find_duplicates(lst):
    counts = {}
    duplicates = set()

    for item in lst:
        if item in counts:
            counts[item] += 1
            if counts[item] == 2:
                duplicates.add(item)
        else:
            counts[item] = 1

    return duplicates

def main():
    list_a = []
    
    while True:
        user_input = input("Digite um valor para adicionar à lista (ou 'skip' para finalizar e ver duplicados): ")
        
        if user_input == 'skip':
            break

        if not user_input.strip():
            print("Entrada vazia ignorada.")
            continue
        
        list_a.append(user_input)
    
    print("Duplicados encontrados:", sorted(find_duplicates(list_a)))
    print('Programa Finalizado')

if __name__ == "__main__":
    main()
