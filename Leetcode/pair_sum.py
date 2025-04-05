# O par de elementos do array deve ser igual a Soma
#[1,2,5,9] = 8 - False
#[1,5,4,4] = 8 - True

def find_pair_with_sum(array, sum_target):
    complement = set()
    for number in array:
        if number in complement:
            return (sum_target - number, number)
        complement.add(sum_target - number)
    return None

def has_pair_with_sum(array, sum_target):
    return find_pair_with_sum(array, sum_target) is not None

def get_pair_with_sum(array, sum_target):
    return find_pair_with_sum(array, sum_target)

def main():
    test_list = [1, 5, 4, 3]
    sum_target = 8
    print(has_pair_with_sum(test_list, sum_target))
    print(get_pair_with_sum(test_list, sum_target))

if __name__ == "__main__":
    main()