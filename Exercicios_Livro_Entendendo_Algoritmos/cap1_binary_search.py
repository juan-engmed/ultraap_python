
def search_target_index_by_binary_search(array, target):
    first_index = 0
    last_index = len(array) - 1

    while first_index <= last_index:
        middle_index = (last_index + first_index) // 2
        guess_value = array[middle_index]

        if guess_value == target:
            return middle_index
        elif guess_value > target:
            last_index = middle_index - 1
        else:
            first_index  = middle_index + 1
    return None        

def main():
    test_list = [1,2,3,4,5]
    target = 11

    target_index = search_target_index_by_binary_search(test_list, target)
    if target_index is not None:
        print(f'O índice do elemento {target} é: {target_index}')
    else:
        print(f'O elemento {target} não foi encontrado na lista.')

if __name__ == "__main__":
    main()