def quicksort(array):
    length = len(array)

    if length <= 1: #Caso base da para evitar Stackover Flow na Recursão
        return array  # Retorna a própria lista (vazia ou com 1 elemento)

    mid_index = (length -1) // 2  #Ja realiza a divisão inteira com arredondamento
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

    #List Comprehension
    # menores_pivot = [x for x in array if x < pivot]
    # iguais_pivot  = [x for x in array if x == pivot]
    # maiores_pivot = [x for x in array if x > pivot]

    return quicksort(menores_pivot) + iguais_pivot + quicksort(maiores_pivot)


def main():
    merge_list = quicksort([4, 3, 7, 9, 2])
    print(merge_list)

if __name__ == "__main__":
    main()
