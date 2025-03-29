def quicksort(array):

    length = len(array)
    if length <= 1:
        return array #Caso Base, para evitarmos Stack overflow

    mid_index = (length -1) //2  #Ja realiza a divisão inteira com arredondamento
    pivot = array[mid_index]
    
    menores_pivot = []
    iguais_pivot = []
    maiores_pivot = []

    for item in array:

        if item < pivot:
            menores_pivot.append(item)
        elif item == pivot:
            iguais_pivot.append(item)
        else:
            maiores_pivot.append(item)

    return quicksort(menores_pivot) + iguais_pivot + quicksort(maiores_pivot)

def main():
    try:
        list_a = [2,0,9]
        list_b = [3,10,2,7]
        union_lists = list_a + list_b
        print(union_lists)

        merge_list = quicksort(union_lists)
        print(merge_list)
    except Exception as ex:
        print(f'Ocorreu um erro, causado por: {ex}')

if __name__ == "__main__":
    main()